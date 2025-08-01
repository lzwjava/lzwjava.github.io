use reqwest::{Client, StatusCode};
use serde_json::{json, Value};
use std::env;

async fn call_mistral_api(prompt: &str, model: &str) -> Option<String> {
    // Get API key from environment variable
    let api_key = match env::var("MISTRAL_API_KEY") {
        Ok(key) => key,
        Err(_) => {
            eprintln!("Error: MISTRAL_API_KEY environment variable not set");
            return None;
        }
    };

    let url = "https://api.mistral.ai/v1/chat/completions";
    let client = Client::new();

    // Construct request payload
    let data = json!({
        "model": model,
        "messages": [{
            "role": "user",
            "content": prompt
        }]
    });

    // Log request details (truncate long prompts for logging)
    println!("Calling Mistral API with model: {}", model);
    println!("Prompt being sent: {}...", &prompt[..prompt.len().min(1000)]);

    // Send request and handle response
    let response = match client
        .post(url)
        .header("Content-Type", "application/json")
        .header("Accept", "application/json")
        .header("Authorization", format!("Bearer {}", api_key))
        .json(&data)
        .send()
        .await
    {
        Ok(resp) => resp,
        Err(e) => {
            eprintln!("Mistral API request failed: {}", e);
            return None;
        }
    };

    // Check response status
    if !response.status().is_success() {
        eprintln!("Mistral API error: Status {}", response.status());
        return None;
    }

    // Parse response JSON
    let response_json = match response.json::<Value>().await {
        Ok(json) => json,
        Err(e) => {
            eprintln!("Mistral API error parsing JSON: {}", e);
            return None;
        }
    };

    // Extract content from response
    response_json
        .get("choices")
        .and_then(|choices| choices.get(0))
        .and_then(|choice| choice.get("message"))
        .and_then(|message| message.get("content"))
        .and_then(|content| content.as_str())
        .map(|content| {
            println!("Mistral API response received");
            content.to_string()
        })
        .or_else(|| {
            eprintln!("Mistral API error: Invalid response format");
            None
        })
}