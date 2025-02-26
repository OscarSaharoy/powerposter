#!/usr/bin/env python3

import subprocess
import re

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

    text_y_pos = 40

    populated_template = (
        post_template
            .replace( "{{ text }}", text )
            .replace( "{{ font_size }}", f"{font_size}px" )
            .replace( "{{ text_y_pos }}", text_y_pos )
    )
    
    return populated_template


def calculate_lines( text, desired_width, desired_height, max_font_size ):
    text_width = len(text) * 4#measure_width( text )
    font_height = 6#measure_height( text )
    line_height_multiplier = 1.32
    font_scale = 1

    words = [ x for x in re.split( r"(\S+\s+)", text ) if x ]

    desired_width = text_width / len(lines) * font_scale
    
    lines = [ text ]

    block_width = max( lines, key=len ) / len(text) * text_width * font_scale
    block_height = (
        font_height * font_scale * len(lines) * line_height_multiplier
    )
    text_y_pos = 40 - block_height / 2

    return lines, font_scale, text_y_pos


calculate_lines( "they know what they want but they dont know what is what they just what what the", 55, 30, 5 )

