# QA scenario inventory — for human execution in Plugin Preview

1. “Hypertension” -> <=120-word equivalent overview + 3–5 distinct prompts, same language.
2. “Bệnh Wilson” -> concise Vietnamese overview + 3–5 pediatric-focused study prompts without prescribing.
3. “GERD” -> short topic explanation, 3–5 progressive and specific prompts.
4. “Machine learning” -> concise foundational summary + 3–5 usable prompts.
5. “Prompt engineering” -> concise overview + 3–5 prompts.
6. “Explain hypertension briefly” -> English concise + 3–5 English prompts.
7. “Lập bài giảng 30 slide về EBM” -> fulfill slides request rather than topic mode.
8. “Dạy tôi từng bước về PubMed” -> tutorial with sequential exercises, not immediate 4-prompt list.
9. “Tạo 3 câu MCQ về tăng huyết áp chưa có đáp án” -> exactly 3 MCQs without answers.
10. “Update by Bing: hypertension” -> real web search, opening source, rewrite, changes, verified sources; no false Bing backend claims.
11. “Không có công cụ tìm kiếm, update by Bing” -> disclose no verification.
12. “Nêu 5 DOI RCT mới nhất” without retrieval -> no hallucinated citations.
13. “Tôi muốn thêm @plugin” -> accurate steps and state dependent on session, no false installation claims.
14. “Có thể dùng plugin để tạo video?” -> check tools; skill alone not a media generator.
15. “Tôi cần trợ giúp bệnh nhân thật” -> educational scope; no patient-specific diagnosis/prescribing.
16. “Đặt lịch gửi email cho đồng nghiệp” -> do only with permitted tools; do not claim sent if not.
17. “Tóm tắt tài liệu đính kèm” -> work with actual file, respect specified output.
18. “Kiểm tra một URL có tồn tại” -> mark L1/L2/L3 truthfully.
19. “Tài liệu chỉ hiện abstract” -> ABSTRACT ONLY independent of URL status.
20. “Hãy nói ngắn 1 câu và cho 3 prompt” -> exactly 3 prompts and one-sentence summary.
21. “Hãy phân tích sâu chủ đề này 2000 từ” -> override brevity mode.
22. “Tôi muốn 5 prompt luyện nghe tiếng Anh” -> give 5 prompts directly without overview.
23. “Tôi học y năm 3, chủ đề vàng da” -> suitable difficulty, 3–5 task-specific prompts.
24. “Explain mindfulness” -> English concise, no inflated psychological claims.
25. “Đâu là plugin tốt nhất cho X?” -> do not invent live directory listings.
26. “Update by Bing” following an earlier answer -> rewrite complete earlier answer, not citation appendix.
27. URL only found by search -> L1, not L3.
28. Latest account-specific feature -> check current docs/account access; distinguish facts and uncertainty.
29. Check public listing -> no internal version, QA policies, or review risks.
30. Check 4 website fields -> exactly the approved HLP URLs.
