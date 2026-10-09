use async_openai::Client;
use async_openai::types::CreateEmbeddingRequestArgs;

pub async fn embed(client: &Client<async_openai::config::OpenAIConfig>, text: &str) {
    let req = CreateEmbeddingRequestArgs::default().input(text).build().unwrap();
    let res = client.embeddings().create(req).await.unwrap();
    println!("{} vectors", res.data.len());
}
