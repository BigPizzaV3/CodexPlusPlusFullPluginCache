\# 売れ筋本データベース設計  
Bestseller Book Structure Database

\#\# 目的  
売れている本の構造を分析し  
出版企画の成功確率を高める。

AIはこのデータから

\- 売れるテーマ  
\- 売れるタイトル構造  
\- 読者変化  
\- 市場強度

を学習する。

\---

\#\# データ構造

1冊 \= 1レコード

以下の情報を保存する。

\---

\#\# 基本情報

Title    
Author    
Publisher    
Year    
AmazonURL    
Genre  

\---

\#\# 市場情報

MarketCategory

例  
健康  
ビジネス  
自己啓発  
お金  
教育

MarketSize

巨大  
大  
中  
小

CompetitionLevel

高  
中  
低

\---

\#\# 読者情報

TargetAge

20代  
30代  
40代  
50代

TargetGender

男性  
女性  
両方

ReaderProblem

例

太っている    
疲れている    
お金がない  

\---

\#\# 変化構造（最重要）

BeforeState    
読む前の状態

AfterState    
読んだ後の状態

TransformationType

習慣    
知識    
成功    
安心  

\---

\#\# タイトル構造

TitlePattern

例

数字    
習慣    
専門家    
最短  

BenefitType

健康    
収入    
時間  

EmotionTrigger

安心    
恐怖    
希望  

\---

\#\# 売れた理由

PainStrength

強  
中  
弱

TransformationStrength

大  
中  
小

Reproducibility

高  
中  
低

AuthorAuthority

高  
中  
低

\---

\#\# 著者強み

AuthorType

医師    
研究者    
成功者    
専門家  

UniqueAsset

臨床経験    
研究    
実体験  

AudienceBase

SNS    
テレビ    
なし  
