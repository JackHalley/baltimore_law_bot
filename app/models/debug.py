from embeddings import tokenizer, answer_question


def debug_tokenization(question, context):
    chunk_size = 400  # tokens
    overlap = 50  # tokens

    # Validate the length of the context
    if len(context) <= 10:
        print("Full context:", context)
        print(f"Context length (characters): {len(context)}")
        print("Warning: Context is too short. Consider providing a longer context.")

    context_tokens = tokenizer.tokenize(context)
    chunk_texts = [context_tokens[i:i + chunk_size] for i in range(0, len(context_tokens), chunk_size - overlap)]

    for idx, chunk in enumerate(chunk_texts):
        chunk_text = tokenizer.convert_tokens_to_string(chunk)
        print(f"Chunk {idx + 1}: {chunk_text[:100]}...")  # Print the beginning of each chunk

    return chunk_texts


def debug_bert():
    test_question = "Who was president of the US in 2021?"
    test_context = "In 2021, Joe Biden became the president of the US after winning the 2020 elections."
    test_answer = answer_question(test_question, test_context)
    print(test_answer)  # Expected: "Joe Biden"


def debug_with_chunks(context):
    chunks = debug_tokenization("affordable housing", context)

    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}: {tokenizer.convert_tokens_to_string(chunk)}")
        sample_answer = answer_question("affordable housing", tokenizer.convert_tokens_to_string(chunk))
        print(f"Answer from chunk {i + 1}: {sample_answer}")
        print('-' * 50)


if __name__ == "__main__":
    # Assuming you have the same context as before
    context = "..."  # Your cleaned and parsed context here

    print("Debugging BERT on a simple test...")
    debug_bert()

    print("\nDebugging with Chunks...")
    debug_with_chunks(context)
