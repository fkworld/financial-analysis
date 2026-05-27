# {公司名} {year}年财报还原分析

> **生成日期**：{generated_date}
>
> **生成模型**：{generated_model}
>
> **源财报文件**：{source_report}
>
> **参考摘要文件**：{summary_file}

---

## 一、核心财务数据

_单位：人民币亿元；比率单位：% 或 ppt；净现比单位：x_

| 指标             |    {prior_year}年(报告)    |    {year}年(报告)    |      报告增速/变动       |      {year}年(还原)      |        还原增速/变动         |
| ---------------- | :------------------------: | :------------------: | :----------------------: | :----------------------: | :--------------------------: |
| 营收             |      {prior_revenue}       |      {revenue}       |      {revenue_yoy}       |      {adj_revenue}       |      {adj_revenue_yoy}       |
| 毛利             |         {prior_gp}         |         {gp}         |         {gp_yoy}         |         {adj_gp}         |         {adj_gp_yoy}         |
| 毛利率           |        {prior_gpm}         |        {gpm}         |        {gpm_chg}         |        {adj_gpm}         |        {adj_gpm_chg}         |
| EBITDA           |       {prior_ebitda}       |       {ebitda}       |       {ebitda_yoy}       |       {adj_ebitda}       |       {adj_ebitda_yoy}       |
| EBITDA率         |   {prior_ebitda_margin}    |   {ebitda_margin}    |   {ebitda_margin_chg}    |   {adj_ebitda_margin}    |   {adj_ebitda_margin_chg}    |
| 扣非净利润       |    {prior_core_profit}     |    {core_profit}     |    {core_profit_yoy}     |    {adj_core_profit}     |    {adj_core_profit_yoy}     |
| 扣非净利率       | {prior_core_profit_margin} | {core_profit_margin} | {core_profit_margin_chg} | {adj_core_profit_margin} | {adj_core_profit_margin_chg} |
| 经营性现金流净额 |        {prior_ocf}         |        {ocf}         |        {ocf_yoy}         |        {adj_ocf}         |        {adj_ocf_yoy}         |
| 净现比           |  {prior_cash_conversion}   |  {cash_conversion}   |  {cash_conversion_chg}   |  {adj_cash_conversion}   |  {adj_cash_conversion_chg}   |
| 自由现金流       |        {prior_fcf}         |        {fcf}         |        {fcf_yoy}         |        {adj_fcf}         |        {adj_fcf_yoy}         |
| 销售费用         |    {prior_selling_exp}     |    {selling_exp}     |      {selling_yoy}       |    {adj_selling_exp}     |      {adj_selling_yoy}       |
| 销售费用率       |    {prior_selling_rate}    |    {selling_rate}    |    {selling_rate_chg}    |    {adj_selling_rate}    |    {adj_selling_rate_chg}    |
| 管理费用         |     {prior_admin_exp}      |     {admin_exp}      |       {admin_yoy}        |     {adj_admin_exp}      |       {adj_admin_yoy}        |
| 管理费用率       |     {prior_admin_rate}     |     {admin_rate}     |     {admin_rate_chg}     |     {adj_admin_rate}     |     {adj_admin_rate_chg}     |
| 研发费用         |       {prior_rd_exp}       |       {rd_exp}       |         {rd_yoy}         |       {adj_rd_exp}       |         {adj_rd_yoy}         |
| 研发费用率       |      {prior_rd_rate}       |      {rd_rate}       |      {rd_rate_chg}       |      {adj_rd_rate}       |      {adj_rd_rate_chg}       |
| 三费率           |     {prior_three_rate}     |     {three_rate}     |     {three_rate_chg}     |     {adj_three_rate}     |     {adj_three_rate_chg}     |
| 固定资产折旧     |       {prior_fa_dep}       |       {fa_dep}       |       {fa_dep_yoy}       |       {adj_fa_dep}       |       {adj_fa_dep_yoy}       |
| 固定资产折旧率   |    {prior_fa_dep_rate}     |    {fa_dep_rate}     |    {fa_dep_rate_chg}     |    {adj_fa_dep_rate}     |    {adj_fa_dep_rate_chg}     |

> 注：固定资产折旧率优先使用固定资产原值口径；若财报未披露，则改用期末固定资产净额口径并注明。EBITDA 应注明是公司披露值还是根据财报项目重构。扣非净利率 = 扣非净利润 / 营收。自由现金流优先采用公司直接披露口径；若未披露，则按“经营性现金流净额 - 资本开支”计算，并注明资本开支取数口径及局限。净现比 = 经营性现金流净额 / 扣非净利润，若分母小于等于 0 则注明“不适用”。若无法基于现有披露可靠计算，保留原指标行并填写“无法有效计算”。核心财务数据表中，仅在 `2025年(还原)` 数值前使用利润方向标记：增加利润用 `🔺`，减少利润用 `🟢`，不影响或无法明确判断则不标记。

## 二、还原项目

| 调整项                         | 报告口径           | 还原口径            | 对核心指标影响       | 证据来源       |
| ------------------------------ | ------------------ | ------------------- | -------------------- | -------------- |
| ① 三费资本化归零、三费摊销移除 | {cap_report_basis} | {cap_restore_basis} | {cap_impact_summary} | {cap_evidence} |
| ② 固定资产综合折旧率固定为15%  | {dep_report_basis} | {dep_restore_basis} | {dep_impact_summary} | {dep_evidence} |

> 注：第①项必须说明当期新增资本化金额、当期摊销金额、对 EBITDA、扣非净利润、经营性现金流净额、自由现金流、三费率的影响；若无法可靠还原经营性现金流净额，必须明确写“无法有效计算现金流还原影响”；若无法可靠还原自由现金流，必须明确写“无法有效计算自由现金流还原影响”。第②项必须说明折旧计提基数、报告折旧率、15%还原折旧额，以及税后利润影响。利润影响描述前使用符号：增加利润用 `🔺`，减少利润用 `🟢`，无影响不加符号。

## 三、结论

1. **{conclusion_1_title}**：{conclusion_1_detail}
2. **{conclusion_2_title}**：{conclusion_2_detail}
3. **{conclusion_3_title}**：{conclusion_3_detail}

> 注：结论重点围绕费用真实负担、盈利质量、现金含量，以及 EBITDA 作为最干净盈利指标的解读；如已披露或可可靠计算，也应结合自由现金流判断现金质量。若存在口径代理、拆分不足或近似估算，必须在结论中再次提示。

---

> **后续步骤**：基于本文件继续生成 `{公司名}-{year}-估值.md`，估值时优先使用本文件中的还原后利润与口径说明。
