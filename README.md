# Learn English App

## 📁 Project Architecture

This project follows a modular, scalable, microservice-oriented architecture designed for a modern AI-powered English learning application.
The system is built using:

NestJS – Main API Backend (business logic)

FastAPI – AI Microservice (NLP, generation, speech processing)

PostgreSQL – Primary database

Redis – Caching, queue tasks, rate limiting

React/Vue – Frontend application (optional mobile client)

🏛 High-Level Architecture
                   ┌───────────────────────────┐
                   │         FRONTEND          │
                   │   React / Vue / Mobile    │
                   └──────────────┬────────────┘
                                  │
                                  ▼
         ┌─────────────────────────────────────────────┐
         │          NESTJS – API GATEWAY (Main)        │
         │─────────────────────────────────────────────│
         │ Auth  │ Users │ Vocabulary │ Learning │ AI   │
         │ Stats │ Words │ Progress   │ Sessions │ Proxy│
         └───────────────┬──────────────────────────────┘
                          │
                          │  REST / gRPC communication
                          ▼
        ┌───────────────────────────────────────────────┐
        │              FASTAPI – AI SERVICE             │
        │───────────────────────────────────────────────│
        │ Grammar │ SentenceGen │ Tenses │ Speech │ AI  │
        │ Check   │ Generator   │ Engine │ toText │ NLP │
        └─────────────────────┬─────────────────────────┘
                              │
             ┌────────────────┴────────────────┐
             ▼                                 ▼
   ┌──────────────────────┐          ┌──────────────────────┐
   │      PostgreSQL      │          │        Redis         │
   │ Main Data Storage    │          │ Cache, Queue, Rate   │
   └──────────────────────┘          └──────────────────────┘

⚙️ Backend Components
1. NestJS – Main Backend

Handles core application logic, authentication, permissions, learning system, and communication with the AI service.

Responsibilities:

User authentication (JWT)

Vocabulary management

Learning session logic (SRS – spaced repetition)

User progress tracking

Grammar check routing (via FastAPI)

Word & sentence generation routing

Statistics and usage analytics

Database operations (PostgreSQL)

Caching and rate limiting (Redis)

WebSocket notifications (optional)

Main Modules:
src/modules/
 ├─ auth/
 ├─ users/
 ├─ vocabulary/
 ├─ learning/
 ├─ progress/
 ├─ stats/
 ├─ ai/
 └─ common/

2. FastAPI – AI Microservice

Dedicated separate microservice for all AI-powered operations.

Responsibilities:

Grammar checking

Sentence generation

Word usage examples

Tenses generation

Speech-to-text (Whisper)

Pronunciation scoring

Next-word suggestion (embeddings)

Folder Structure:
fastapi_app/
 ├─ routers/
 ├─ services/
 ├─ models/
 ├─ utils/
 └─ main.py

🗄 Database Design (PostgreSQL)
Main Tables:

users

vocabulary

word_examples

word_progress

learning_sessions

ai_logs (optional)

Example schema:

users
├ id
├ email
├ password
├ settings (jsonb)
└ created_at

vocabulary
├ id
├ user_id
├ word
├ translation
├ definition
├ part_of_speech
└ added_at

🚀 Redis Usage

Redis is used for:

Caching AI results

Caching vocabulary data

Speech processing task queue

User session data

API rate limiting

🔌 Service Communication
NestJS → FastAPI

Communication happens via:

REST
Simple microservice calls

gRPC (optional)
For low latency model inference

Internal network (Docker compose / Kubernetes)

Example request flow:

Frontend → NestJS (POST /ai/sentence)

NestJS → FastAPI (POST /sentence/generate)

FastAPI → LLM model → returns result

NestJS caches result → returns to client

🐳 Deployment Architecture (Docker)

All services run inside Docker containers:

docker-compose.yml
 ├─ frontend        (React/Vue)
 ├─ nest-backend    (API Gateway)
 ├─ fastapi-ai      (AI Microservice)
 ├─ postgres        (database)
 ├─ redis           (cache)
 └─ nginx           (reverse proxy)

📦 Advantages of This Architecture

✔️ Highly scalable
✔️ AI load isolated from business logic
✔️ Easy to deploy with Docker
✔️ Secure API gateway (NestJS)
✔️ Modular and maintainable codebase
✔️ Real-time performance with Redis
✔️ Can support large user bases
✔️ Easy to extend (add new AI models / modules)