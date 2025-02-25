#!/usr/bin/env python3

import subprocess

with open("text-template.svg") as f:
    text_template = f.read()

with open("post-template.svg") as f:
    post_template = f.read()


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

def assemble_post( text ):
    text_width = measure_width( text )
    text_height = measure_height( text )

    desired_width = 65 - 9
    scale = desired_width / text_width
    font_size = 4 * scale

    populated_template = post_template.replace( "{{ text }}", text ).replace( "{{ font_size }}", f"{font_size}px" )
    
    return populated_template


print( assemble_post( "cheeeeeeeeeese" ))
