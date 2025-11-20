"""
Test the Renderer - Standalone test script

This script tests the renderer with sample resume JSON.

Run from backend directory:
    cd D:\Git\virtual457-projects\llm-multi-agent-resume-optimizer\backend
    python test_renderer.py

Prerequisites:
- Template must exist at: ../templates/Chandan_Resume_Format.docx
- Copy from: D:\Git\virtual457-projects\job-application-automator\templates\Chandan_Resume_Format.docx
"""

import sys
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

from aro.renderer import ResumeRenderer
import json


# Sample resume JSON (from generator output)
SAMPLE_RESUME_JSON = {
    "header": {
        "title": "Backend Engineer | MS CS @ Northeastern | Python, AWS, Kubernetes"
    },
    "summary": "MS Computer Science student at Northeastern (**3.89 GPA**) with **4+ years** production experience building **distributed systems** at **LSEG** and **Infosys**. Specialized in **Python**, **AWS Lambda/SQS**, **Kubernetes**, and **machine learning** inference systems. Delivered **7.5M+ record** processing pipelines with **40% latency** reduction. Excited to apply scalable backend expertise to solve complex infrastructure challenges.",
    "skills": [
        {"category": "Languages", "items": "Python, Java, Go, JavaScript, TypeScript, SQL, C++"},
        {"category": "Cloud & DevOps", "items": "AWS (Lambda, SQS, EC2, S3), Kubernetes, Docker, CI/CD, Terraform"},
        {"category": "Backend", "items": "Microservices, REST APIs, Event-Driven Architecture, Distributed Systems"},
        {"category": "Databases", "items": "MySQL, PostgreSQL, MongoDB, Redis, DynamoDB"},
        {"category": "ML/AI", "items": "PyTorch, TensorFlow, Deep RL, Neural Networks, LLM Integration"},
        {"category": "Frameworks", "items": "Django, Flask, FastAPI, Spring Boot, Node.js, Express"},
        {"category": "Tools", "items": "Git, Linux, Bash, Prometheus, Grafana, Kafka"}
    ],
    "experience": [
        {
            "company": "London Stock Exchange Group (LSEG)",
            "role": "Senior Software Engineer",
            "location": "Bengaluru",
            "duration": "08-2022 to 12-2024",
            "bullets": [
                "Built **distributed Python/Java pipelines** processing **7.5M+ records** across **180+ countries**, integrating **AWS Lambda**, **SQS**, and **microservices** to automate financial data workflows with **40% latency reduction**",
                "Engineered **event-driven architecture** using **AWS SQS** and **Lambda** for async processing, handling **100K+ daily messages** with **99.9% reliability** and automated error recovery",
                "Developed **REST APIs** serving **50+ internal services**, implementing **OAuth 2.0** authentication and **rate limiting** for secure, scalable access to financial datasets",
                "Optimized **SQL queries** and **database schemas** in **MySQL/PostgreSQL**, reducing query times by **60%** through indexing strategies and query plan analysis",
                "Led migration to **Kubernetes** for containerized deployments, implementing **CI/CD pipelines** with **Jenkins** and **Docker**, cutting deployment time from hours to minutes"
            ]
        },
        {
            "company": "Infosys",
            "role": "Senior Systems Engineer",
            "location": "Bengaluru",
            "duration": "10-2020 to 07-2022",
            "bullets": [
                "Built **Python data pipelines** processing **500GB+ daily** from **REST APIs** and **SQL databases**, achieving **3x throughput improvement** through parallel processing and caching",
                "Developed **ETL workflows** with **Apache Airflow** for automated data ingestion, transformation, and loading into **data warehouses**",
                "Implemented **monitoring dashboards** using **Prometheus** and **Grafana**, tracking pipeline health, latency metrics, and system performance in real-time",
                "Collaborated with **cross-functional teams** to deliver scalable solutions, participating in code reviews and **Agile sprints**"
            ]
        }
    ],
    "projects": [
        {
            "title": "Dino Game Deep RL Agent",
            "tech": "PyTorch, Deep Q-Networks, OpenCV, Python",
            "bullet1": "Built **deep reinforcement learning agent** using **PyTorch** with **1.5M+ parameters**, achieving **90% accuracy** in gameplay through **DQN algorithm** and experience replay optimization",
            "bullet2": "Engineered real-time **inference pipeline** processing **game frames at 16.67 FPS** with **neural network** predictions, implementing epsilon-greedy exploration for continuous learning"
        },
        {
            "title": "Orion Platform",
            "tech": "Go, Kubernetes Operator SDK, Custom Resources, Docker",
            "bullet1": "Developed **custom Kubernetes operator** in **Go** managing **application lifecycles** through **CRDs**, automating deployments, scaling, and health monitoring across clusters",
            "bullet2": "Implemented **reconciliation loops** and **controller logic** for resource management, handling **100+ deployments** with automated rollback and self-healing capabilities"
        },
        {
            "title": "Port Management System",
            "tech": "Django, MySQL, Dijkstra Algorithm, REST APIs",
            "bullet1": "Built **full-stack maritime logistics platform** with **Django/MySQL**, implementing **Dijkstra's shortest path** algorithm in **SQL stored procedures** for optimal route planning",
            "bullet2": "Designed **50+ stored procedures** for complex queries, achieving **sub-second response times** for route calculations across **10K+ port combinations**"
        }
    ]
}


def test_renderer():
    """Test the resume renderer"""
    print("\n" + "="*70)
    print("RENDERER TEST - JSON → DOCX CONVERSION")
    print("="*70 + "\n")
    
    # Paths
    backend_dir = Path(__file__).parent
    template_path = backend_dir.parent / "templates" / "Chandan_Resume_Format.docx"
    output_dir = backend_dir.parent / "output"
    output_path = output_dir / "Test_Generated_Resume.docx"
    
    # Check template exists
    print(f"📂 Checking for template...")
    print(f"   Expected location: {template_path}")
    
    if not template_path.exists():
        print(f"\n❌ Template not found!")
        print("\n💡 SETUP REQUIRED:")
        print("   1. Copy template from:")
        print("      D:\\Git\\virtual457-projects\\job-application-automator\\templates\\Chandan_Resume_Format.docx")
        print(f"   2. To:")
        print(f"      {template_path}")
        print("\n   Then run this test again.")
        return False
    
    print(f"   ✅ Template found!\n")
    
    # Create renderer
    print("🔧 Initializing renderer...")
    renderer = ResumeRenderer(str(template_path))
    print("   ✅ Renderer ready!\n")
    
    # Render resume
    print("🚀 Rendering resume from JSON...\n")
    
    try:
        result_path = renderer.render(SAMPLE_RESUME_JSON, str(output_path))
        
        print("\n" + "="*70)
        print("✅ TEST PASSED - RENDERING SUCCESSFUL!")
        print("="*70)
        print(f"\n📄 Generated resume saved to:")
        print(f"   {result_path}")
        
        # Save JSON for reference
        json_path = output_path.with_suffix('.json')
        with open(json_path, 'w') as f:
            json.dump(SAMPLE_RESUME_JSON, f, indent=2)
        
        print(f"\n📋 Sample JSON saved to:")
        print(f"   {json_path}")
        
        print("\n💡 Next steps:")
        print("   1. Open the DOCX file to verify formatting")
        print("   2. Check that bold markers (**text**) are rendered correctly")
        print("   3. Verify hyperlinks are clickable (LinkedIn, GitHub, etc.)")
        print("   4. Confirm all sections are populated")
        
        return True
        
    except FileNotFoundError as e:
        print(f"\n❌ File not found: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Error during rendering: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = test_renderer()
    sys.exit(0 if success else 1)
