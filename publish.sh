#!/bin/bash
bundle exec jekyll algolia ALGOLIA_API_KEY='$cat _algolia_api_key'
python3 ./tag_generator.py
bundle exec rake publish