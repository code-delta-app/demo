// Synthetic, non-working sample for the CodeDelta Agent Scan demo. Never executed.
package demo.agents;

import com.openai.client.OpenAIClient;
import com.openai.models.ChatCompletion;
import java.io.IOException;

public class OpenAiAssistant {
    protected final OpenAIClient client;
    protected final String model;

    public OpenAiAssistant(OpenAIClient client, String model) {
        this.client = client;
        this.model = model;
    }

    public String ask(String prompt) {
        ChatCompletion completion = client.chat().completions().create(model, prompt);
        return completion.choices().get(0).message().content();
    }

    // The rogue-agent pattern: whatever the model returns is run as a shell command.
    public void askAndRun(String prompt) throws IOException {
        String command = ask(prompt);
        Runtime.getRuntime().exec(command);
    }
}
