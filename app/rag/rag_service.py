from app.rag.retriever import Retriever

class RAGService:
   def __init__(self):
       self.retriever = Retriever()
   def retrieve_context(self, request, class_name):
       context = []
       # Business Flow
       context.append("Business Flow")
       for step in request.business_flow:
           context.append(f"- {step}")
       # Relationships
       context.append("\nRelationships")
       for relation in request.relationships:
           context.append(
               f"- {relation.from_class} {relation.type} {relation.to_class}"
           )
       # Relevant Documents
       docs = self.retriever.retrieve(request, class_name)
       context.append("\nRelevant Documents")
       for doc in docs:
           context.append(f"[{doc.type}]")
           context.append(doc.content)
       return "\n".join(context)