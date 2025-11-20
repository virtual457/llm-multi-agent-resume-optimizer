# LMARO API Documentation

## Base URL
```
http://localhost:8000
```

## Authentication
None (for now)

---

## Endpoints

### 1. Generate Resume

**Endpoint:** `POST /api/generate`

**Description:** Generate optimized resume for a job description

**Request Body:**
```json
{
  "username": "chandan",
  "jd_text": "Full job description text...",
  "company": "Google",
  "role": "Software Engineer Intern",
  "optimize": true  // Optional, default true
}
```

**Response:**
```json
{
  "success": true,
  "resume": {
    "header": {...},
    "summary": "...",
    "skills": [...],
    "experience": [...],
    "projects": [...]
  },
  "scores": {
    "evaluation": 92,
    "factuality": 98
  },
  "paths": {
    "json": "database/resumes/chandan/job1.json",
    "docx": "output/chandan_job1.docx"
  }
}
```

---

### 2. Evaluate Resume

**Endpoint:** `POST /api/evaluate`

**Description:** Evaluate existing resume against JD

**Request Body:**
```json
{
  "username": "chandan",
  "job_id": "job1"
}
```

**Response:**
```json
{
  "total_score": 85,
  "keyword_score": 30,
  "llm_score": 55,
  "section_scores": {
    "experience": 20,
    "skills": 18,
    "projects": 12,
    "presentation": 5
  },
  "feedback": "Overall assessment...",
  "section_feedback": {
    "experience": "...",
    "skills": "...",
    "projects": "...",
    "presentation": "..."
  }
}
```

---

### 3. Check Factuality

**Endpoint:** `POST /api/factuality`

**Description:** Verify resume claims against user profile

**Request Body:**
```json
{
  "username": "chandan",
  "job_id": "job1"
}
```

**Response:**
```json
{
  "is_factual": true,
  "factuality_score": 95,
  "issues": [],
  "summary_check": {
    "is_accurate": true,
    "issues": []
  },
  "experience_check": {...},
  "projects_check": {...},
  "skills_check": {...}
}
```

---

### 4. Get Resume

**Endpoint:** `GET /api/resume/{username}/{job_id}`

**Description:** Retrieve generated resume

**Response:**
```json
{
  "resume": {...},
  "metadata": {
    "username": "chandan",
    "job_id": "job1",
    "updated_at": "2025-11-19T10:30:00"
  }
}
```

---

### 5. Upload User Profile

**Endpoint:** `POST /api/user/upload`

**Description:** Upload user profile JSON

**Request:** Form data with file upload
- Field: `file` (profile.json)
- Query param: `username`

**Response:**
```json
{
  "success": true,
  "message": "Profile uploaded",
  "username": "chandan",
  "path": "database/chandan/profile.json"
}
```

---

### 6. Create Job

**Endpoint:** `POST /api/job/create`

**Description:** Create job description

**Request Body:**
```json
{
  "job_id": "job2",
  "company": "Microsoft",
  "role": "SWE Intern",
  "jd_text": "Full job description..."
}
```

**Response:**
```json
{
  "success": true,
  "job_id": "job2",
  "path": "database/jobs/job2.json"
}
```

---

### 7. List Jobs

**Endpoint:** `GET /api/jobs`

**Description:** List all available jobs

**Response:**
```json
{
  "jobs": [
    {
      "job_id": "job1",
      "company": "Test Company",
      "role": "Backend Engineer"
    },
    {
      "job_id": "job2",
      "company": "Microsoft",
      "role": "SWE Intern"
    }
  ]
}
```

---

### 8. List Resumes

**Endpoint:** `GET /api/resumes/{username}`

**Description:** List all resumes for a user

**Response:**
```json
{
  "username": "chandan",
  "resumes": [
    {
      "job_id": "job1",
      "company": "Test Company",
      "role": "Backend Engineer",
      "updated_at": "2025-11-19T10:30:00"
    }
  ]
}
```

---

### 9. Health Check

**Endpoint:** `GET /api/health`

**Description:** Check API status

**Response:**
```json
{
  "status": "healthy",
  "gemini_api": "available",
  "version": "0.1.0"
}
```

---

## Error Responses

All endpoints return errors in this format:

```json
{
  "success": false,
  "error": "Error message",
  "detail": "Detailed error information"
}
```

**Common Status Codes:**
- `200` - Success
- `400` - Bad request (invalid input)
- `404` - Not found (user/job/resume doesn't exist)
- `500` - Server error
- `503` - Gemini API unavailable

---

## Usage Examples

### Generate Resume
```bash
curl -X POST http://localhost:8000/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "username": "chandan",
    "jd_text": "Software Engineer Intern...",
    "company": "Google",
    "role": "SWE Intern"
  }'
```

### Get Resume
```bash
curl http://localhost:8000/api/resume/chandan/job1
```

### Upload Profile
```bash
curl -X POST http://localhost:8000/api/user/upload?username=chandan \
  -F "file=@profile.json"
```

---

## Notes

- All POST requests require `Content-Type: application/json`
- File uploads use `multipart/form-data`
- Large operations (generate, evaluate) may take 30-60 seconds
- API is single-threaded (one request at a time)
