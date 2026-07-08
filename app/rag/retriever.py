class Retriever:
   
   def retrieve(self, request, class_name):
       documents = []
       if request.rag:
           for doc in request.rag.documents:
               if class_name.lower() in doc.content.lower():
                   documents.append(doc)
       return documents