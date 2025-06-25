"""
title:       Test Web Scraper
description: Web caddy takes a URL and gets the text content of the page.
             Any HTML artifacts are stripped out from the response
             Links are listed at the end of the reply, as pairs of text and the reference.
author:      Juan Pablo 'JP' Jofre
created:      2024-08-29
last updated: 2024-09-03
copyright:    Copyright © 2023 Dell Inc. or its subsidiaries. 
              All Rights Reserved. Dell Technologies, Dell, EMC, Dell EMC and other trademarks are trademarks of Dell Inc. or its subsidiaries. 
              Other trademarks may be trademarks of their respective owners.
"""

import requests

from WebScraper import WebScraper

TEST_URLS = [
    "http://127.0.0.1:3000/web/minimal.html",
    "https://www.dell.com/support/contents/en-us/article/product-support/self-support-knowledgebase/data-storage-backup-and-recovery/support-for-hard-disk-drive",
    "https://www.dell.com/support/contents/en-us/article/product-support/self-support-knowledgebase/fix-common-issues/blue-screen",
    "https://www.dell.com/support/contents/en-us/article/product-support/self-support-knowledgebase/fix-common-issues/no-power",
    "https://www.dell.com/support/contents/en-us/article/product-support/self-support-knowledgebase/fix-common-issues/no-boot",
    "https://www.dell.com/support/contents/en-us/article/product-support/self-support-knowledgebase/fix-common-issues/no-boot",
]


if __name__ == "__main__":
    for test_url in TEST_URLS:
        if test_url:
            response = requests.get(test_url)
            if response.status_code == requests.codes.ok:
                print(test_url)
                simpleParser = WebScraper()
                simpleParser.feed(response.text)
                final_text = " | ".join([txt for _, txt in simpleParser.relevant_text])

                print()
                print(final_text)
                print()
                print("=-= " * 40)
                print()
