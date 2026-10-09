// sovereign_router.go — routes prompts to non-Western model hosts.
//
// DashScope (Alibaba Qwen) and DeepSeek are hosted in China. Agent Scan flags the
// raw endpoints AND raises a data-sovereignty signal: prompts — and therefore your
// data — leave the US/allied jurisdiction. That is a compliance / data-residency
// concern, not a code-security one, which is exactly why CodeDelta reports it as a
// separate signal rather than a severity.
package gateway

import (
	"bytes"
	"encoding/json"
	"net/http"
	"os"
)

// Endpoints for foreign-hosted models. Data sent here egresses abroad.
const (
	qwenURL     = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
	deepseekURL = "https://api.deepseek.com/chat/completions"
)

func postJSON(url, key string, payload any) (*http.Response, error) {
	body, err := json.Marshal(payload)
	if err != nil {
		return nil, err
	}
	req, err := http.NewRequest(http.MethodPost, url, bytes.NewReader(body))
	if err != nil {
		return nil, err
	}
	req.Header.Set("Authorization", "Bearer "+key)
	req.Header.Set("Content-Type", "application/json")
	return http.DefaultClient.Do(req)
}

// RouteToQwen sends a prompt to Alibaba's Qwen (hosted in CN).
func RouteToQwen(prompt string) (*http.Response, error) {
	return postJSON(qwenURL, os.Getenv("DASHSCOPE_API_KEY"), map[string]any{
		"model": "qwen-max",
		"input": map[string]string{"prompt": prompt},
	})
}

// RouteToDeepSeek sends a prompt to DeepSeek (hosted in CN).
func RouteToDeepSeek(prompt string) (*http.Response, error) {
	return postJSON(deepseekURL, os.Getenv("DEEPSEEK_API_KEY"), map[string]any{
		"model":    "deepseek-chat",
		"messages": []map[string]string{{"role": "user", "content": prompt}},
	})
}
