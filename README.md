# pt-nutricional-ensemble-classifier
Portuguese Nutricional Ensemble Classifier 
How to Use the API
Run the script on your local machine or server:

python pt_nutricional_classifier_api.py

Send a POST request with food nutrition data:

curl -X POST "http://localhost:5000/predict" -H "Content-Type: application/json" -d '{"Proteínas [g]": 10.2, "Hidratos de carbono [g]": 5.1, "Lípidos [g]": 2.3}'
Response Format:
json

{
    "Predicted Category": "Legumes"
}

How to Deploy with Docker
Build the Docker image:

docker build -t food_classifier_api .
Run the container:

docker run -p 5000:5000 food_classifier_api
Access the API at:

http://localhost:5000/predict
