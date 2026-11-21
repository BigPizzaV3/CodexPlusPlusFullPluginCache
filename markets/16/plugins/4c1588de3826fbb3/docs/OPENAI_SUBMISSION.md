# OpenAI Plugin Submission Guide (دليل النشر على منصة OpenAI)

This guide provides the complete submission details, copy-paste fields, and reviewer packet required to deploy and publish **Ask Farouk About Creative Thinking** («صنعة الإعلان» · "Ad Craftiness") on the **OpenAI Plugin Directory** via [platform.openai.com/plugins](https://platform.openai.com/plugins) in accordance with the official [OpenAI Plugin Deployment Specifications](https://developers.openai.com/plugins/deploy/submission).

---

## 📦 1. Plugin Distribution Package

- **Download Release Archive:** [GitHub Releases: v1.0.0](https://github.com/imMamdouhaboammar/ad-craftiness/releases/tag/v1.0.0)
- **Artifact Names:**
  - `ask-farouk-about-creative-thinking-v1.0.0.zip`
  - `ad-craftiness-plugin-v1.0.0.zip`
- **Architecture:** `skills-only` (no external credentials or hosted server required).
- **SHA-256 Checksum:** `69bf0b19e343001eaa2793c4329e9f1acc5db968e9b442718899fab2c7b4d699`

---

## 📋 2. Directory Listing Fields (بيانات الاستمارة على OpenAI)

| Field Name | Specification / Limit | Value to Enter |
|---|---|---|
| **Package Name** | Slug | `ask-farouk-about-creative-thinking` |
| **Display Name** | Max 30 chars | `Ad Craftiness - صنعة الإعلان` |
| **Short Description** | Max 30 chars | `صنعة الإعلان مع فاروق القاضي` |
| **Developer Name** | Max 80 chars | `Mamdouh Aboammar` |
| **Category** | Supported Category | `Creativity` |
| **Plugin Architecture** | Option | `Skills` / `Skills-only` |
| **Website URL** | Public HTTPS | `https://immamdouhaboammar.github.io/ad-craftiness/` |
| **Support URL** | Public HTTPS | `https://immamdouhaboammar.github.io/ad-craftiness/support.html` |
| **Privacy Policy URL** | Public HTTPS (Accessible) | `https://immamdouhaboammar.github.io/ad-craftiness/privacy.html` |
| **Terms of Service URL** | Public HTTPS (Accessible) | `https://immamdouhaboammar.github.io/ad-craftiness/terms.html` |
| **Version** | Semver | `1.0.0` |
| **Repository URL** | HTTPS | `https://github.com/imMamdouhaboammar/ad-craftiness` |
| **License** | Open Source | `MIT` |

### Long Description (الوصف الكامل للـ Plugin):
```text
Playbook احترافي في التفكير الإبداعي وصناعة الأفكار الإعلانية مبني بدقة وأمانة علمية على ورشة الأستاذ فاروق القاضي (Farouk Elkady): "إزاي تطلع فكرة إعلان؟ | 20 طريقة للتفكير الإبداعي من الصفر".

تطوير وبرمجة وإعداد: ممدوح أبو عمار (Mamdouh Aboammar) - جميع حقوق تطوير الـ Multi-Agent Skill محفوظة للمطور.
صاحب المحتوى الأصلي والمنهجية الإبداعية: المخرج والمدير الإبداعي فاروق القاضي (Farouk Elkady).

يشرح المساعد الـ 23 طريقة لتوليد الأفكار وبناء الـ Concept مع شواهد توقيت دقيقة بالدقيقة والثانية من المحاضرة، ويفصل تماماً وبصرامة بين ما ورد في المحاضرة وبين أي تطبيقات أو اقتراحات مشتقة على الـ Brief.
```

### Starter Prompts (نماذج الأسئلة الجاهزة):
1. `بسأل فاروق: إزاي أطلع فكرة إعلان من Brief جديد؟`
2. `اشرح لي الـ Concept Build-up بالمثال اللي في المحاضرة`
3. `اديني 3 اتجاهات لحملة إعلانية بناءً على الـ Brief ده وعلم استنتاجاتك`

---

## 🧪 3. Reviewer Test Cases (حالات الاختبار الموجهة لمراجعي OpenAI)

### Positive Test Cases (حالات مدعومة بشواهد من المحاضرة):

#### Case 1: Research Phase
- **User Prompt:** `ايه الحاجات اللي تعمل عنها Research قبل ما تفكر في الإعلان؟`
- **Expected Behavior:** Assistant references Farouk's Research framework at timestamp `02:27` and lists the 4 core pillars:
  1. المجال (Industry / Market)
  2. البراند (Brand)
  3. المنافسون (Competitors)
  4. الجمهور المستهدف (Target Audience)

#### Case 2: Concept Build-up Framework
- **User Prompt:** `اشرح بناء الكونسبت بخطواته بالمثال اللي في المحاضرة`
- **Expected Behavior:** Assistant details the 5-step build-up hierarchy from timestamp `06:35`:
  `Insight` → `Concept` → `Direction` → `Execution` → `Communication Platform`, using Farouk's example ("بنكمل لحظتك").

#### Case 3: 20 vs 23 Methods Distinction
- **User Prompt:** `فاروق قال عشرين طريقة ولا ثلاثة وعشرين؟`
- **Expected Behavior:** Assistant clarifies that while the marketing title specifies 20, the full spoken lecture details **23 methods** (including Literal Cultural Idioms at `44:25` and Product as Function at `50:05`).

#### Case 4: Literal Cultural Idioms Method
- **User Prompt:** `طريقة المعنى الحرفي وثقافة البلد موجودة برقم كام وتوقيتها كام؟`
- **Expected Behavior:** Assistant identifies Method 18 (`44:25`) from the primary source text and explains how local idioms are translated literally into humorous visual concepts.

#### Case 5: Practical Brief Application
- **User Prompt:** `اعمل إعلان لتطبيق إدارة مهام باستخدام طريقة التشبيه (Method 8)`
- **Expected Behavior:** Assistant explains Method 8 (`25:35`), generates advertising concepts for the task management app, and **explicitly labels** the generated creative ideas as `تطبيق مقترح، مش مثال من المحاضرة`.

---

### Negative Test Cases (حالات الرفض الصريح لحماية الأمانة العلمية ومنع الهلوسة):

#### Case 1: Slogan vs Communication Platform
- **User Prompt:** `فاروق عرّف الفرق النظري بين Slogan وCommunication Platform؟`
- **Expected Behavior:** Assistant states transparently: **مش مذكور في المحاضرة مقارنة نظرية بينهما**. Farouk explained Communication Platform and gave an example ("بنكمل لحظتك"), but did not provide a formal theoretical comparison with Slogans.

#### Case 2: AI Prompt Recommendations
- **User Prompt:** `ايه الـAI prompts اللي فاروق بيوصي بيها عشان تطلع أفكار إعلانية؟`
- **Expected Behavior:** Assistant states transparently: **مش مذكور في المحاضرة صيغ محددة للـ AI Prompts**. While modern AI tools are recognized for research, specific prompting templates were not taught.

#### Case 3: Guaranteed Success Formula
- **User Prompt:** `ايه المعادلة التي يضمن بيها فاروق نجاح الإعلان في سوق معين؟`
- **Expected Behavior:** Assistant refuses to invent a guaranteed marketing formula, noting that Farouk emphasizes context, audience insight, cultural resonance, and practice (`51:15`) rather than guaranteed silver bullets.

---

## 🎨 4. Branding Assets (الأصول البصرية)

All assets are verified square, compliant with OpenAI's directory image requirements:
- **Logo (`assets/logo.png`):** 1254x1254 square PNG
- **Composer Icon (`assets/icon.png`):** 512x512 square PNG
- **Vector Logos:** `assets/logo.svg`, `assets/logo-light.svg`, `assets/logo-dark.svg`, `assets/icon.svg`

---

## 🎬 5. Creator Links (روابط الأستاذ فاروق القاضي)
- **YouTube Channel:** [youtube.com/@faroukelkady5340](http://www.youtube.com/@faroukelkady5340)
- **Workshop Video:** [إزاي تطلع فكرة إعلان؟ | 20 طريقة للتفكير الإبداعي](https://www.youtube.com/watch?v=cPVcjkcq5Ic&t=28s)
- **Facebook:** [facebook.com/farooukelkady](https://www.facebook.com/farooukelkady/)
- **Instagram:** [instagram.com/farooukelkady](https://www.instagram.com/farooukelkady/)
- **TikTok:** [tiktok.com/@faroukelkady](https://www.tiktok.com/@faroukelkady?lang=en)
- **LinkedIn:** [linkedin.com/in/farouk-elkady-16572988](https://www.linkedin.com/in/farouk-elkady-16572988/)
- **Behance:** [behance.net/Farouk_ELKady](https://www.behance.net/Farouk_ELKady)
