# The Peak Crawler

Automatic playlist generator for Spotify.

## Features

See the [changelog](./CHANGELOG.md) to know all the features supported.

## Development Environment

This project is configured to use the state of the art Python tools for code enforcement, such as `mypy`, `flake8`, and others, underlying the `pre-commit` git hook. So, it's recommended to use the proper extensions in your IDE to increase the productivity.

With your setup done, first you need to install the development dependencies:

```bash
pip install -r requirements.dev.txt
```

Next, install the git hooks:

```bash
pre-commit install
```

Now, before every commit, your code will be checked following the rules defined on `.pre-commit-config.yaml`.

To run the code enforcement scripts manually, just use the `make` for that.
