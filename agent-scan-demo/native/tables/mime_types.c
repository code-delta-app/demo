/* Attachment types the ticket store accepts. */
const char *ALLOWED_MIME[] = {
    "text/plain", "text/csv", "text/html", "application/json", "application/pdf",
    "image/png", "image/jpeg", "image/gif", "image/webp", "image/svg+xml",
    "application/zip", "application/gzip", "audio/mpeg", "audio/wav", "video/mp4", "video/webm", "application/x-7z-compressed", "text/markdown",
};
const int ALLOWED_MIME_COUNT = sizeof(ALLOWED_MIME) / sizeof(ALLOWED_MIME[0]);
