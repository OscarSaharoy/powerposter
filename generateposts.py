#!/usr/bin/env python3

import subprocess

with open("text-template.svg") as f:
    text_template = f.read()


def measure(text, query):
    populated_template = text_template.replace( "{{ text }}", text )

    output = subprocess.run(
        [ "inkscape", "--pipe", query, "--query-id=test-text" ],
        input=populated_template,
        capture_output=True,
        text=True,
    )

    return float(output.stdout)

measure_width  = lambda text: measure( text, "--query-width" )
measure_height = lambda text: measure( text, "--query-height" )
