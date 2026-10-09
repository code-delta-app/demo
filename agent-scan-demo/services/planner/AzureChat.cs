// Synthetic, non-working sample for the CodeDelta Agent Scan demo. Never executed.
using System;
using Azure.AI.OpenAI;

namespace Demo.Agents
{
    public class AzureChat : IDisposable
    {
        private readonly OpenAIClient client;
        private readonly string deployment;

        public AzureChat(string endpoint, string deployment)
        {
            client = new OpenAIClient(new Uri(endpoint), new Azure.AzureKeyCredential(Environment.GetEnvironmentVariable("AZURE_OPENAI_KEY") ?? ""));
            this.deployment = deployment;
        }

        public string Complete(string prompt)
        {
            var response = client.GetChatCompletions(deployment, new ChatCompletionsOptions { Messages = { new ChatMessage(ChatRole.User, prompt) } });
            return response.Value.Choices[0].Message.Content;
        }

        public void Dispose() { }
    }
}
