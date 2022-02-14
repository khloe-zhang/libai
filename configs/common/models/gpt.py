from libai.config import LazyCall

from libai.models.gpt_model import GPTModel, GPTForPreTraining

cfg = dict(
    vocab_size=30522,
    hidden_size=768,
    hidden_layers=24,
    num_attention_heads=12,
    intermediate_size=4096,
    hidden_dropout_prob=0.1,
    attention_probs_dropout_prob=0.1,
    max_position_embeddings=512,
    num_tokentypes=0,
    add_pooling_layer=True,
    initializer_range=0.02,
    layernorm_eps=1e-5,
    bias_gelu_fusion=True,
    bias_dropout_fusion=True,
    scale_mask_softmax_fusion=False,
    apply_query_key_layer_scaling=True,
    fp16=False,
)

cfg = dict(
    num_layers=6,
    vocab_size=30522,
    hidden_size=384,
    ffn_hidden_size=1536,
    num_attention_heads=12,
    max_seq_length=1024,
    embedding_dropout_prob=0,
    attention_dropout_prob=0,
    output_dropout_prob=0,
    layernorm_epsilon=1e-5,
    initializer_range=0.2,
    use_scaled_init_for_output_weights=True,
    bias_gelu_fusion=False,
    bias_dropout_fusion=False,
    scale_mask_softmax_fusion=False,
    apply_query_key_layer_scaling=False,
)

gpt_model = LazyCall(GPTModel)(cfg=cfg)

pretrain_model = LazyCall(GPTForPreTraining)(cfg=cfg)
