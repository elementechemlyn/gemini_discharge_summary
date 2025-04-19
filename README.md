# Discharge Maker

## Introduction

This project is the start of experiments in using LLMs to generate synthetic health data.

Currently, it uses the Gemini API to generate HTML discharge summaries based on the PRSB example:
https://theprsb.org/standards/edischargesummary/#examples

The PDF included in this repository is copyright of the PRSB.

## Usage

- Set your Gemini API Key into the environment variable GEMINI_API_KEY
- Optionally, set the Gemini model you want to use into the environment variable GEMINI_MODEL. The default is gemini-2.5-flash-preview-04-17
- Optionally, set the number of documents you want to create into the environment variable NUM_OUTPUTS. The default is 10.

Run the `oneshot.py` script to generate discharge summaries using a single example prompt which gives a single example (the PRSB example).  The prompt is harcdoded in the source file.

Example outputs are included in the outputs/oneshot folder if you don't want to generate your own.
