#  infer.py
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os

# Try to load the fine-tuned model, fallback to base model if not found
model_base_path = "lora-tinyllama"
base_model = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

if os.path.exists(model_base_path):
    # Find checkpoint directories
    checkpoints = [d for d in os.listdir(model_base_path) if d.startswith("checkpoint-") and os.path.isdir(os.path.join(model_base_path, d))]
    
    if checkpoints:
        # Get the latest checkpoint by number
        latest_checkpoint = max(checkpoints, key=lambda x: int(x.split("-")[1]))
        model_name = os.path.join(model_base_path, latest_checkpoint)
        print(f"Found checkpoints: {checkpoints}")
        print(f"Loading fine-tuned model from {model_name}")
        model = AutoModelForCausalLM.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
    else:
        print(f"No checkpoints found in {model_base_path}, using base model: {base_model}")
        model = AutoModelForCausalLM.from_pretrained(base_model)
        tokenizer = AutoTokenizer.from_pretrained(base_model)
else:
    print(f"Fine-tuned model directory not found at {model_base_path}, using base model: {base_model}")
    model = AutoModelForCausalLM.from_pretrained(base_model)
    tokenizer = AutoTokenizer.from_pretrained(base_model)

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

prompt = "### Instruction:\n What services do you offer.\n\n### Response:"
result = pipe(
    prompt, 
    max_new_tokens=50,  # Reduced for more concise output
    do_sample=True,
    temperature=0.1,    # Lower temperature for more focused responses
    pad_token_id=tokenizer.eos_token_id,
    eos_token_id=tokenizer.eos_token_id
)

# Extract only the response part
generated_text = result[0]["generated_text"]
response = generated_text.split("### Response:")[-1].strip()
print(f"Response: {response}")

# infer.py
# from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
# import os

# model_base_path = "lora-tinyllama"
# base_model = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# if os.path.exists(model_base_path):
#     checkpoints = [d for d in os.listdir(model_base_path) if d.startswith("checkpoint-")]
#     if checkpoints:
#         latest_checkpoint = max(checkpoints, key=lambda x: int(x.split("-")[1]))
#         model_path = os.path.join(model_base_path, latest_checkpoint)
#         print(f"Loading fine-tuned model from {model_path}")
#     else:
#         print("No checkpoints found, using base model.")
#         model_path = base_model
# else:
#     print("LoRA directory not found, using base model.")
#     model_path = base_model

# model = AutoModelForCausalLM.from_pretrained(model_path)
# tokenizer = AutoTokenizer.from_pretrained(model_path)

# pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

# def chat_with_model(user_input):
#     prompt = f"### Instruction:\n{user_input}\n\n### Response:"
#     result = pipe(
#         prompt,
#         max_new_tokens=100,
#         do_sample=True,
#         temperature=0.2,
#         pad_token_id=tokenizer.eos_token_id,
#         eos_token_id=tokenizer.eos_token_id
#     )
#     generated_text = result[0]["generated_text"]
#     response = generated_text.split("### Response:")[-1].strip()
#     return response

# # Example use:
# while True:
#     user_msg = input("You: ")
#     if user_msg.lower() in ["exit", "quit"]:
#         break
#     print("Bot:", chat_with_model(user_msg))
 