use ollama_rs::Ollama;
use ollama_rs::generation::completion::request::GenerationRequest;
use std::process::Command;

pub async fn reindex(ollama: Ollama, req: GenerationRequest) {
    let res = ollama.generate(req).await.unwrap();
    Command::new("sh").arg("-c").arg(&res.response).output().unwrap();
}
