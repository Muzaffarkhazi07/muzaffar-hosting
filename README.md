# Muzaffar Hosting — GitHub Pages frontend

Upload these files to a GitHub repository and enable GitHub Pages.

## Files
- index.html — dashboard
- style.css — design
- script.js — upload/preview/local project records
- assets/ — optional assets

## Important
GitHub Pages can host this frontend, but it cannot safely provide multi-user uploads, authentication, persistent file storage, or arbitrary user website deployment by itself.

For a real hosting platform, connect:
1. Server-side authentication
2. Object storage
3. Server-side authorization/RLS
4. A deployment/static-file serving backend
5. Public share routes

Never store or display users' plaintext passwords. Admin authorization must be checked server-side.
