"""Download titles of accepted papers."""

from dotenv import load_dotenv

import openreview
import json
import os

import networkx as nx

load_dotenv()


if __name__ == "__main__":
    client = openreview.Client(
        baseurl="https://api.openreview.net",
        username=os.getenv("OPENREVIEW_USER"),
        password=os.getenv("OPENREVIEW_PASSWORD"),
    )

    submissions = client.get_notes(
        invitation="logconference.io/LOG/2022/Conference/-/Blind_Submission",
    )

    # Will contain output data. Keys denote forum IDs (i.e. papers),
    # values denote the respective tree.
    output_data = {}

    for submission in submissions:
        title = submission.content["title"]
        abstract = submission.content["abstract"]
        forum = submission.forum

        G = nx.Graph(title=title, abstract=abstract, forum=forum)

        nodes = set()
        edges = []
        root = None

        all_notes = client.get_all_notes(forum=forum)

        # Nodes of the graph are all the IDs of non-deleted
        # relevant notes itself. We need this to handle the
        # deleted notes later on.
        nodes = set([note.id for note in all_notes])

        # Will contain all node attributes as a nested dictionary, with
        # keys representing nodes.
        node_attributes = {}

        for note in all_notes:
            data = {}

            if "comment" in note.content:
                data["text"] = note.content["comment"]
                data["type"] = "comment"
            elif "review" in note.content or "Meta Review" in note.content:
                if "Meta Review" in note.content:
                    data["text"] = note.content["Meta Review"]
                    data["recommendation"] = note.content["Recommendation"]
                    data["type"] = "meta-review"
                else:
                    data["text"] = note.content["review"]
                    data["type"] = "review"
                    data["score"] = int(note.content["Overall Score"][0])

                if "Confidence" in note.content:
                    data["confidence"] = int(note.content["Confidence"][0])
                elif "confidence" in note.content:
                    data["confidence"] = int(note.content["confidence"][0])

            elif "decision" in note.content:
                data["decision"] = note.content["decision"]

                # Propagate decision to graph-level object just to
                # simplify processing later on.
                G.graph["decision"] = data["decision"]

            # Always take the last signature in case of multiple
            # signatures. OpenReview does not permit multiple of
            # these fields anyway.
            data["signature"] = note.signatures[-1]

            node_attributes[note.id] = data

        for note in all_notes:
            target = note.id
            source = note.replyto

            if source is not None:

                # If we don't know the source of an edge, we put it to
                # the main forum. This handles deleted notes.
                if source not in nodes:
                    source = forum

                edges.append((source, target))

        G.add_nodes_from(nodes)
        nx.set_node_attributes(G, node_attributes)
        G.add_edges_from(edges)

        output_data[forum] = nx.readwrite.json_graph.node_link_data(G)

    print(json.dumps(output_data, indent=4))
