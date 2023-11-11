# :technologist: Question and Answering Application Backend

Welcome to the Question and Answering Application Backend, where it primary objective is to serve as the backbone for a personalized question answering platform. This platform empowers you to enhance your knowledge and skills in any subject of your choice.

I'm continuously enhancing this project to provide you with a comprehensive set of features, including:

- **Question Creation**: Craft and submit your own questions to the platform.
- **Answer Management**: Append answers to questions, creating a valuable knowledge base.
- **AI-Powered Answer Generation**: Leverage AI technology to automatically generate answers for your questions.
- **Space Repetition Algorithm**: Employ a spaced repetition algorithm to optimize your learning and memory retention.
- **Local Datastore**: Designed with a focus on personal use, we provide a local datastore. Should you desire, you can easily switch to a MySQL database by modifying the configuration. Thanks to our ORM, transitioning to different databases is straightforward.
- **Vector Database Connection**: Streamline question retrieval with a vector database connection, making it easier to locate your questions.
- **User Registration**: Sign up for a personalized experience and track your progress.
- **Tag Registration**: Categorize questions for easy retrieval, even without AI assistance.
- **AI-Based Question Creation**: Generate questions based on existing text context, making learning more intuitive.
- **AI-Powered Answer Correction**: Utilize AI to improve the accuracy of your answers.
- **AI-Duplication Detector**: Utilize AI to detect which question is duplicated. Besides we could search for exact same text, is better to search for very similar questions.

As of now, this backend operates without a queue system, ensuring that every request is handled synchronously for a seamless user experience.

# Flow

1. Register a user
2. Register a question (vinculado to the user)
3. Register a tag to question
4. Register the relationship between tag and question
5. Register a answer (vinculado to the question)
