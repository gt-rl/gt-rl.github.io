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
    data = {}

    for submission in submissions:
        title = submission.content["title"]
        abstract = submission.content["abstract"]
        forum = submission.forum

        G = nx.DiGraph(title=title, abstract=abstract, forum=forum)

        nodes = set()
        edges = []
        root = None

        all_notes = client.get_all_notes(forum=forum)

        # Nodes of the graph are all the IDs of non-deleted
        # relevant notes itself. We need this to handle the
        # deleted notes later on.
        nodes = set([note.id for note in all_notes])

        for note in all_notes:
            target = note.id
            source = note.replyto
            invite = note.invitation.split("/")[-1]

            if source is not None:

                # If we don't know the source of an edge, we put it to
                # the main forum. This handles deleted notes.
                if source not in nodes:
                    source = forum

                edges.append((source, target, {"type": invite}))
            else:
                root = target

        G.add_nodes_from(nodes)
        G.add_edges_from(edges)

        data[forum] = nx.readwrite.json_graph.tree_data(G, root)

    print(json.dumps(data, indent=4))
