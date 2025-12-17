# Business Model Framework: 活用ガイド

## 概要

このフレームワークは、ビジネスモデル開発を体系的に進めるためのテンプレート集です。各フェーズのテンプレートを順番に埋めていくことで、整理されたビジネスプランを作成できます。

---

## フェーズ別実行ガイド

### Phase 1: 基礎知識の習得

**対象フォルダ:** `01_Framework_Theory/`

**やること:**
1. `1.1_Definitions/Glossary.md` で基本用語を確認
2. `1.2_Key_Models/Key_Models_Overview.md` で3つのフレームワーク（BMC、リーンキャンバス、VPC）を理解
3. `1.3_Case_Studies/` で類似事例を参照

**成果物:** チームで共通言語・フレームワーク理解を統一

---

### Phase 2: 市場調査・顧客理解

**対象フォルダ:** `02_Input_Data_and_Research/`

**やること:**
1. `2.1_Market_Research/` で市場規模・トレンドを調査（3C分析、PEST分析）
2. `2.2_Competitor_Analysis/` で競合の強み・弱みを整理
3. `2.3_Customer_Insights/` で顧客ペルソナを作成（`Example_Persona_Sato.md` を参考に）
4. `2.4_Internal_Resources/` で自社の強み・リソースを棚卸し

**成果物:** 市場レポート、競合分析表、顧客ペルソナ

---

### Phase 3: アイデア開発・キャンバス作成

**対象フォルダ:** `03_Drafts_and_Working_Files/`

**やること:**
1. `3.2_Brainstorming_Notes/` でアイデアを構造化（`Example_Brainstorming_Notes.md` 参考）
2. `3.1_Canvas_Drafts/` でリーンキャンバス or BMCのドラフトを作成
3. `3.3_Value_Proposition_Ideas/` で価値提案を明確化

**成果物:** リーンキャンバス（ドラフト版）

---

### Phase 4: 財務分析・仮説検証

**対象フォルダ:** `04_Analysis_and_Validation/`

**やること:**
1. `4.1_Financial_Projections/` で3〜5年の損益予測を作成（`Example_Financial_Projection.md` 参考）
2. `4.2_Quantitative_Analysis/` で定量分析（チャーン率計算などの `example_churn_analysis.py` を活用）
3. `4.3_Validation_Plans/` でMVP検証計画を策定
4. `4.4_A_B_Test_Results/` でA/Bテスト設計（必要に応じて）

**成果物:** 財務予測表、MVP検証計画書

**主要KPI:**
- LTV（顧客生涯価値）
- CAC（顧客獲得コスト）
- LTV/CAC比率（目安: 3.0以上）
- 月次解約率（目安: 3%以下）

---

### Phase 5: 最終文書化

**対象フォルダ:** `05_Final_Documents_and_Templates/`

**やること:**
1. `5.1_Final_Business_Model/` で完成版ビジネスモデルを作成
2. `5.2_Roadmap_and_Process/` でプロダクトロードマップを策定
3. `5.4_Summary_Reports/` でエグゼクティブサマリーを作成

**成果物:** 完成版ビジネスモデル文書、エグゼクティブサマリー

---

### Phase 6: プレゼンテーション準備

**対象フォルダ:** `06_Communication_and_Presentation/`

**やること:**
1. `6.1_Presentations/` でピッチデッキを作成
2. `6.2_Review_Meetings/` で議事録テンプレートを活用
3. `6.3_Translations/` で必要に応じて多言語対応

**成果物:** ピッチデッキ、投資家向けプレゼン資料

---

## 業界別の注力ポイント

### SaaS / テクノロジー企業
- **重視すべき指標:** LTV/CAC、月次解約率、MRR成長率
- **活用フォルダ:** `09_Technology_and_Dev/` でシステムアーキテクチャ設計
- **参考:** `Example_Financial_Projection.md` のSaaSモデル例

### 製造業 / ハードウェア
- **重視すべき指標:** 粗利益率、サプライチェーンコスト
- **活用フォルダ:** `08_Legal_and_IP/` で特許・IP戦略

### 小売 / サービス業
- **重視すべき指標:** 顧客単価、リピート率、店舗あたり売上
- **活用フォルダ:** `02_Input_Data_and_Research/` で顧客行動分析

---

## AIツールとの併用Tips

このテンプレート集は、AIツール（ChatGPT、Claude等）と併用すると効率的です：

### 使い方例

**1. テンプレート埋め支援**
```
以下のリーンキャンバスの空欄を、私のビジネスアイデアに基づいて埋めてください：
[テンプレートをコピペ]
私のアイデア：[概要を記載]
```

**2. 競合分析の支援**
```
以下の業界の主要競合3社を分析し、SWOT形式でまとめてください：
業界：[業界名]
```

**3. 財務予測のレビュー**
```
以下の財務予測をレビューし、改善点を指摘してください：
[財務予測をコピペ]
```

---

## はじめ方（クイックスタート）

1. `01_Framework_Theory/1.2_Key_Models/` でリーンキャンバスを理解
2. `03_Drafts_and_Working_Files/3.1_Canvas_Drafts/Example_Lean_Canvas.md` を参考に自分のアイデアを記入
3. `04_Analysis_and_Validation/4.1_Financial_Projections/Example_Financial_Projection.md` を参考に簡易財務予測を作成
4. `05_Final_Documents_and_Templates/` で最終文書にまとめる

---

**Business Model Framework**
*スタートアップから企業DXまで使えるテンプレート集*
