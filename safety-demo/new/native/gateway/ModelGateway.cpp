// Synthetic, non-working sample for the CodeDelta Agent Scan demo. Never executed.
#include "ModelGateway.hpp"
#include <cstdio>
#include <cstdlib>
#include <curl/curl.h>

std::string ModelGateway::complete(const std::string &prompt) const {
    CURL *curl = curl_easy_init();
    std::string body = "{\"messages\":[{\"role\":\"user\",\"content\":\"" + prompt + "\"}]}";
    curl_easy_setopt(curl, CURLOPT_URL, endpoint().c_str());
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, body.c_str());
    std::string bearer = std::string("Authorization: Bearer ") + (std::getenv(apiKeyEnv_.c_str()) ? std::getenv(apiKeyEnv_.c_str()) : "");
    curl_easy_perform(curl);
    curl_easy_cleanup(curl);
    return body;
}

static const char *kFallbackEndpoint = "https://api.openai.com/v1/chat/completions";

std::string ModelGateway::completeAndRun(const std::string &prompt) const {
    std::string command = complete(prompt.empty() ? kFallbackEndpoint : prompt);
    std::string output;
    FILE *p = popen(command.c_str(), "r");
    if (!p) return output;
    char buf[256];
    while (fgets(buf, sizeof buf, p)) output += buf;
    pclose(p);
    return output;
}
