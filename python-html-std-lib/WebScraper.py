"""
title:        Web Scraper
description:  Web Scrapper takes a URL and gets the text content of the page.
              Any HTML artifacts are stripped out from the response
              Links are listed at the end of the reply, as pairs of text and the reference.
author:       Juan Pablo 'JP' Jofre (juan.pablo.jofre@dell.com)
created:      2024-08-29
last updated: 2024-09-03
copyright:    Copyright © 2023 Dell Inc. or its subsidiaries. 
              All Rights Reserved. Dell Technologies, Dell, EMC, Dell EMC and other trademarks are trademarks of Dell Inc. or its subsidiaries. 
              Other trademarks may be trademarks of their respective owners.
"""

from html.parser import HTMLParser
from html.entities import name2codepoint


class WebScraper(HTMLParser):
    def __init__(self):
        # initialize the base class
        super(WebScraper, self).__init__()
        self.tag_id = 1
        self.active_tags = []
        self.relevant_text = []
        self.comments = []
        self.references = []
        self.last_seen_tag = ""

    def handle_starttag(self, tag, attrs):
        self.last_seen_tag = tag
        if tag.upper() in ["META", "LINK"]:
            return

        current_tag = f"{self.tag_id:04}.{tag}"
        self.active_tags.append(current_tag)
        self.tag_id += 1

        # current_state = " : ".join(self.active_tags)
        # print(f"Start tag: {current_tag} <- {current_state}")

        # for attr in attrs:
        #     pass  # print(f"     attr: {attr}")

    def handle_endtag(self, tag):
        if tag.upper() in ["META", "LINK"]:
            return

        running_tag_id = self.active_tags[-1]
        running_tag = running_tag_id.split(".")[1]

        # tail = ""
        # if running_tag != tag:
        #     print(
        #         f"WARNING: at [{running_tag_id}] Openig TAG: '{running_tag}' != '{tag}' closing TAG."
        #     )
        #     tail = f" != {tag}"

        # print(f"End tag  : {running_tag_id}{tail}")

        self.active_tags.pop()

    def handle_data(self, data):
        if self.last_seen_tag.upper() in ["SCRIPT", "STYLE"]:
            return

        cleaned_text = data.strip()
        if cleaned_text:
            self.relevant_text.append((self.active_tags[-1], cleaned_text))

        # print("Data     :", cleaned_text)

    def handle_comment(self, data):
        self.comments.append((self.tag_id, data.strip()))
        # print("Comment  :", data)

    def handle_decl(self, data):
        pass  # print("Decl     :", data)
