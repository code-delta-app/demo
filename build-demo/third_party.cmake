# SYNTHETIC DEMO FILE — a build file that fetches remote content at build
# time, planted so CodeDelta's fetch tier has something to flag in the demo
# PR. The URL is an RFC 2606 reserved example domain: nothing is ever fetched.
file(DOWNLOAD https://downloads.example.com/vendored/libdemo-1.2.tar.gz
     ${CMAKE_BINARY_DIR}/libdemo.tar.gz
     EXPECTED_HASH SHA256=0000000000000000000000000000000000000000000000000000000000000000)
