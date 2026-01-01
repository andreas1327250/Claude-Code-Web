#!/usr/bin/env python3
"""
Simple HTTP server for testing the ÖBB Train Availability App
Usage: python3 server.py
Then open http://localhost:8000 in your browser
"""

import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server running at http://localhost:{PORT}/")
    print(f"Open http://localhost:{PORT}/ in your browser")
    print("Press Ctrl+C to stop the server")
    httpd.serve_forever()
