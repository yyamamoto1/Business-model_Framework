# Usage Guide: Business Model Framework

## 段階的活用ガイド (Step-by-Step Guide)

このフレームワークは、ビジネスモデル開発の思考プロセスに沿って設計されています。以下のステップで活用することをお勧めします。

### Step 1: 基礎理論の学習と共通認識の形成
- **場所:** `01_Framework_Theory/`
- **アクション:**
    1. プロジェクト開始前に、チームメンバー全員で主要なビジネスモデルフレームワーク（BMC, Lean Canvas等）の理論を確認します。 (`1.2_Key_Models/`)
    2. プロジェクト内で使用する用語の定義を統一し、`1.1_Definitions/` に用語集としてまとめます。
    3. 関連する業界の成功・失敗事例を `1.3_Case_Studies/` に集め、学びを抽出します。

### Step 2: 情報収集と現状分析
- **場所:** `02_Input_Data_and_Research/`
- **アクション:**
    1. 市場規模、成長率、トレンドなどのマクロな情報を `2.1_Market_Research/` に集約します。
    2. 競合他社の強み・弱み、戦略を分析し、`2.2_Competitor_Analysis/` にSWOT分析などの形式で保存します。
    3. ターゲット顧客へのインタビューやアンケートを実施し、その生データを `2.3_Customer_Insights/` に格納します。ここからペルソナを作成します。
    4. 自社の技術、人材、ブランドなどのリソースを `2.4_Internal_Resources/` にリストアップします。
> **Hint:** 各フォルダにある `Example_*.md` ファイルが、具体的な記入例として参考になります。

### Step 3: アイデア創出とプロトタイピング
- **場所:** `03_Drafts_and_Working_Files/`
- **アクション:**
    1. Step 2の情報を基に、チームでブレインストーミングを行い、議事録やメモを `3.2_Brainstorming_Notes/` に保存します。
    2. ビジネスモデルキャンバスやリーンキャンバスのドラフトを `3.1_Canvas_Drafts/` で複数パターン作成します。
    3. 提供価値の具体的なアイデアを `3.3_Value_Proposition_Ideas/` に書き出します。
> **Hint:** 各フォルダにある `Example_*.md` ファイルが、具体的な記入例として参考になります。

### Step 4: 分析と仮説検証
- **場所:** `04_Analysis_and_Validation/`
- **アクション:**
    1. ドラフトモデルの収益性とコスト構造を `4.1_Financial_Projections/` で試算します。
    2. 市場データや顧客データを基に、`4.2_Quantitative_Analysis/` で定量的な分析を行います。（必要であればPythonスクリプト等もここに保存）
    3. 最も重要な仮説を検証するためのMVP（Minimum Viable Product）の計画を `4.3_Validation_Plans/` で設計します。
    4. A/Bテストなどの検証結果を `4.4_A_B_Test_Results/` に記録し、学びを次に活かします。
> **Hint:** 各フォルダにある `Example_*.md` ファイルが、具体的な記入例として参考になります。

### Step 5: 最終化とドキュメント整備
- **場所:** `05_Final_Documents_and_Templates/`
- **アクション:**
    1. 検証を経て磨き上げられた最終版のビジネスモデルを `5.1_Final_Business_Model/` に格納します。
    2. 実行に向けた具体的なロードマップやプロセスを `5.2_Roadmap_and_Process/` にまとめます。
    3. 今後別のプロジェクトで再利用できるテンプレート（空白のキャンバスなど）を `5.3_Templates/` に保存します。
> **Hint:** 各フォルダにある `Example_*.md` ファイルが、具体的な記入例として参考になります。

### Step 6: 共有とコミュニケーション
- **場所:** `06_Communication_and_Presentation/`
- **アクション:**
    1. 投資家や経営陣、チームメンバーなど、相手に合わせたプレゼンテーション資料を `6.1_Presentations/` で作成・管理します。
    2. 定期的なレビュー会議でのフィードバックや決定事項を `6.2_Review_Meetings/` に記録します。
> **Hint:** 各フォルダにある `Example_*.md` ファイルが、具体的な記入例として参考になります。

---

## 業界別カスタマイズ例 (Industry-Specific Customization)

### SaaS / デジタルプロダクト
- `09_Technology_and_Dev/` の利用を推奨します。
    - `9.1_System_Architecture/`: スケーラビリティを考慮した技術選定やアーキテクチャ図を格納。
    - `9.2_User_Stories_and_Reqs/`: 機能要件やユーザーストーリーを詳細に記述。
    - `9.3_MVP_Prototypes/`: FigmaやSketchなどのプロトタイプファイルを格納。
- `04_Analysis_and_Validation/`: LTV（顧客生涯価値）やCAC（顧客獲得コスト）、チャーンレートの分析を重点的に行います。

### 製造業 / ハードウェア
- `08_Legal_and_IP/` の重要度が高まります。
    - `8.2_IP_Strategy/`: 製品の独自性を守るための特許戦略を管理。
    - `8.3_Contract_Templates/`: サプライヤーとの契約書テンプレートを格納。
- `02_Input_Data_and_Research/`: サプライチェーンや製造コストに関する調査が重要になります。

### 小売 / サービス業
- `02_Input_Data_and_Research/` の `2.3_Customer_Insights/` が特に重要です。
    - 顧客の店舗での行動観察や、サービス体験のジャーニーマップを作成します。
- `04_Analysis_and_Validation/`: 店舗ごとの売上分析や、キャンペーンの効果測定（A/Bテスト）が中心となります。

---
*このガイドはあくまで一例です。プロジェクトの特性に合わせて、自由にカスタマイズしてご活用ください。*
