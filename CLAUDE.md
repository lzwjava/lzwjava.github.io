# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
This is a static website project hosted on GitHub Pages. It consists of HTML files served directly without any build process. The site is automatically deployed via GitHub Actions when changes are pushed to the main branch.

## Architecture
- **Frontend**: Pure HTML5 with basic semantic structure and navigation
- **Deployment**: Automated via GitHub Actions to GitHub Pages
- **Hosting**: Serverless static hosting through GitHub Pages

## Key Files
- `index.html`: Main webpage with header, navigation, content sections, and footer
- `.github/workflows/static.yml`: CI/CD pipeline for GitHub Pages deployment
- `README.md`: Project documentation

## Development Commands
Since this is a static HTML project, there are no build processes, linters, or automated tests currently configured. Basic development involves:
- Editing HTML files directly
- Pushing to main branch for automatic deployment

## GitHub Pages Deployment
The project uses GitHub Actions for automated deployment:
- Triggers on push to main branch
- Deploys the entire repository as static content
- Accessible at [username].github.io repository URL

## Common Tasks
- **Local Development**: Open HTML files in browser or use `python -m http.server` for local hosting
- **Deployment**: Push to main branch to trigger automatic deployment
- **Content Updates**: Edit `index.html` and commit changes