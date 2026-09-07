// Synthetic, non-working sample for the CodeDelta Agent Scan demo. Never executed.
package demo.agents;

import dev.langchain4j.model.chat.ChatLanguageModel;
import com.openai.client.OpenAIClient;
import java.util.List;

public class SupportAgent extends OpenAiAssistant {
    private final ChatLanguageModel fallback;

    public SupportAgent(OpenAIClient client, ChatLanguageModel fallback) {
        super(client, "gpt-4o");
        this.fallback = fallback;
    }

    // An AI call inside a loop: one ticket, one model round-trip, no cap on the bill.
    public void triage(List<String> tickets) {
        for (String ticket : tickets) {
            String verdict = ask("Classify this support ticket: " + ticket);
            if (verdict.isEmpty()) {
                verdict = fallback.generate(ticket);
            }
            System.out.println(verdict);
        }
    }
}
