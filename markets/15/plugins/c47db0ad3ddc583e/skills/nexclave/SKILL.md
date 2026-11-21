---
name: nexclave
description: Access Nexclave enterprise AI engineering services, AI products (RKE, Omni Vision, Email Triage, YOLO Vision), technology capabilities, and consultation inquiries.
---

# Nexclave Enterprise AI Assistant Skill

Use this skill whenever users ask about Nexclave, enterprise AI integration, ready-to-ship AI products, or want to audit and automate their workflows with native AI.

## Available Capabilities & Routing Guidance

### 1. Company Information & Principles
- Use `get_company_overview` with section filters (`summary`, `principles`, `mission`, `why_nexclave`, `stats`) to answer questions about Nexclave's corporate identity, foundational philosophy, and positioning as "The Engine Of Native AI Enterprise".
- For contact and office location queries, use `get_contact_info`.

### 2. Enterprise Services & Consultation
- Use `get_services` to list available engineering services (e.g., Workflow Development, MCP Integration, Agentic AI, Fine-Tuning, On-Premise AI, System Integration, Responsible AI).
- Use `get_service_details` with `service_name` for in-depth architecture, deliverables, and operational scope.

### 3. Purpose-Built AI Products
- Use `get_ai_products` to explore Nexclave's ready-to-ship product suite:
  - **RKE (Reliable Knowledge Engine)**: No-code RAG platform for knowledge bases, vector search, and retrieval pipelines.
  - **Omni Vision**: Zero-UI incident reporting platform utilizing image capture, location, and timestamp for automated routing.
  - **Email Triage**: Centralized AI email classification and intelligent routing engine.
  - **YOLO Vision**: End-to-end computer vision platform for collecting, annotating, training, and deploying object detection models.

### 4. Technology Stack & 31 Capabilities
- Use `get_technology_capabilities` to filter across 5 categories:
  - `Artificial Intelligence`
  - `AI Engineering`
  - `Enterprise Engineering`
  - `Data Systems`
  - `Responsible AI`
- Use the `query` argument to search for specific technologies such as RAG, Vector Databases, MCP, Kubernetes, LoRA, etc.

### 5. Engagement Models & How We Work
- Use `get_engagement_levels` to explain engagement tiers:
  - **Level 01 (Eye-Opener Study)**: Free assessment of operational bottlenecks and high-ROI opportunities.
  - **Level 02 (Surface-Level Study)**: Paid documentation-focused system study with High-Level Architecture (HLA) and roadmap.
  - **Level 03 (Deep-Dive Study & Dev)**: Complete end-to-end transformation, custom model development, integration, and SLAs.
- Use `get_delivery_methodology` to describe the 6-stage delivery process (Understand, Identify, Design, Build, Integrate, Transform).
- Use `get_responsible_ai_framework` for governance, safety fences, and ISO/IEC 42001 & 23894 readiness.

### 6. Inquiries & Free AI Audit Requests
- Use `get_inquiry_requirements` to check required details before submission.
- Use `submit_inquiry` when the user wants to commission an audit or contact sales/engineering. Provide the generated ticket ID and SLA response guarantee (< 24 business hours).

