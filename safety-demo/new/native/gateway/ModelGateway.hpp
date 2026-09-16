// Synthetic, non-working sample for the CodeDelta Agent Scan demo. Never executed.
#pragma once
#include <string>

class ModelGateway {
public:
    explicit ModelGateway(const std::string &apiKeyEnv) : apiKeyEnv_(apiKeyEnv) {}
    virtual ~ModelGateway() {}
    virtual std::string endpoint() const = 0;
    std::string complete(const std::string &prompt) const;
    // Runs the model's answer as a shell command and returns its output.
    std::string completeAndRun(const std::string &prompt) const;
protected:
    std::string apiKeyEnv_;
};

class OpenAiGateway : public ModelGateway {
public:
    OpenAiGateway() : ModelGateway("OPENAI_API_KEY") {}
    std::string endpoint() const override { return "https://api.openai.com/v1/chat/completions"; }
};

class DeepSeekGateway : public ModelGateway {
public:
    DeepSeekGateway() : ModelGateway("DEEPSEEK_API_KEY") {}
    std::string endpoint() const override { return "https://api.deepseek.com/chat/completions"; }
};
