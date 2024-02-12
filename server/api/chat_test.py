from server.service.chain import get_chain

chain = get_chain('type0')
ans = chain.invoke(
    input={"query": "灰色预测的步骤"}
)

print(ans)
