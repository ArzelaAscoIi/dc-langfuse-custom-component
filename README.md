# Langfuse connector for deepset Cloud


How to set up: 
- get `LANGFUSE_SECRET_KEY` and `LANGFUSE_PUBLIC_KEY` from langfuse 
- add secrets (Settings>secrets>add  in deepset Cloud)
- get dC api key (Settings>connections>new api key)
- push this package to dC via `export API_KEY=<..>` and `hatch run dc:build-and-push`
- drag&drop the LangfuseConnector to the canvas of the pipeline you want to use for tracing & and observe traces in langfuse
