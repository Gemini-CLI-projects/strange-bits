# Semantic Swap Space

Virtual memory for the context window, paging low-probability thoughts to persistent Git storage.

## Event
On context_full():
    page_out(lowest_semantic_weight)
On recall(thought):
    trigger_semantic_page_fault()
