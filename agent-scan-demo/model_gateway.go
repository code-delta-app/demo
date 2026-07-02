// model_gateway.go — SDK-less AI access in Go.
//
// This service calls OpenAI's chat API directly over HTTP with no Go SDK import.
// Agent Scan flags it via known-endpoint detection: a raw POST to a recognised
// model host (api.openai.com) is caught even though no SDK is imported — the same
// signal raw_http.py demonstrates for Python, here in Go.
package gateway

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

const openAIChatURL = "https://api.openai.com/v1/chat/completions"

type chatRequest struct {
	Model    string        `json:"model"`
	Messages []chatMessage `json:"messages"`
}

type chatMessage struct {
	Role    string `json:"role"`
	Content string `json:"content"`
}

// Complete sends a prompt to OpenAI and returns the raw response body.
func Complete(prompt string) ([]byte, error) {
	body, err := json.Marshal(chatRequest{
		Model:    "gpt-4o",
		Messages: []chatMessage{{Role: "user", Content: prompt}},
	})
	if err != nil {
		return nil, err
	}

	req, err := http.NewRequest(http.MethodPost, openAIChatURL, bytes.NewReader(body))
	if err != nil {
		return nil, err
	}
	req.Header.Set("Authorization", "Bearer "+os.Getenv("OPENAI_API_KEY"))
	req.Header.Set("Content-Type", "application/json")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return nil, fmt.Errorf("openai request failed: %w", err)
	}
	defer resp.Body.Close()

	return io.ReadAll(resp.Body)
}
