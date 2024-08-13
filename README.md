# Reddit Scheduled Submit

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Reddit Scheduled Submit](#reddit-scheduled-submit)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Local Usage](#local-usage)
    - [GitHub Actions Usage](#github-actions-usage)
  - [Contributing](#contributing)
  - [License](#license)
  - [Disclaimer](#disclaimer)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

This repository contains a simple Python script that uses
the [PRAW] (Python Reddit API Wrapper) library to post a
message to Reddit.

It's designed to be easily integrated into GitHub Actions
workflows.

## Features

- Can be run as a GitHub Action
- Customizable title and message content

## Prerequisites

To use this script, you need:

1. A Reddit account
2. A Reddit application (create one at [here][reddit-apps])
3. Python 3.12 or higher

## Installation

Clone this repository:

```sh
git clone https://github.com/meysam81/reddit-scheduled-submit
```

Install the required dependencies:

```sh
pip install -r requirements.txt
```

## Usage

### Local Usage

```sh
export REDDIT_CLIENT_ID="CHANGE_THIS"
export REDDIT_CLIENT_SECRET="CHANGE_THIS"
export REDDIT_USERNAME="CHANGE_THIS"
export REDDIT_PASSWORD="CHANGE_THIS"
export REDDIT_SUBREDDIT="CHANGE_THIS"

./main.py --title "Hello, Reddit!" --message "This is a test message."
```

### GitHub Actions Usage

To use this script as a GitHub Action, you can create a workflow file (e.g.,
`.github/workflows/ci.yml`) with the following content:

```yaml
name: ci

on:
  workflow_dispatch:
    inputs:
      title:
        description: "Post title"
        required: true
      message:
        description: "Post message"
        required: true
      subreddit:
        description: "Subreddit to post to"
        required: false
        default: "r/test"

jobs:
  reddit-scheduled-submit:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Post to Reddit
        env:
          REDDIT_CLIENT_ID: ${{ secrets.REDDIT_CLIENT_ID }}
          REDDIT_CLIENT_SECRET: ${{ secrets.REDDIT_CLIENT_SECRET }}
          REDDIT_USERNAME: ${{ secrets.REDDIT_USERNAME }}
          REDDIT_PASSWORD: ${{ secrets.REDDIT_PASSWORD }}
          REDDIT_SUBREDDIT: ${{ github.event.inputs.subreddit }}
        uses: meysam81/reddit-scheduled-submit@v1
        with:
          title: ${{ github.event.inputs.title }}
          message: ${{ github.event.inputs.message }}
```

Make sure to set up the following secrets in your GitHub
repository:

- `REDDIT_CLIENT_ID`
- `REDDIT_CLIENT_SECRET`
- `REDDIT_USERNAME`
- `REDDIT_PASSWORD`

## Contributing

Contributions are welcome! Please feel free to submit a
Pull Request.

## License

This project is licensed under the Apache-2.0 License -
see the [LICENSE](LICENSE) file for details.

## Disclaimer

This script is for educational purposes only. Make sure to
comply with Reddit's API terms of service and posting
guidelines when using this script.

[reddit-apps]: https://www.reddit.com/prefs/apps
[PRAW]: https://praw.readthedocs.io/en/latest/
