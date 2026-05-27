# {公司名} {year}年财务摘要

> **生成日期**：{generated_date}
>
> **生成模型**：{generated_model}
>
> **源财报文件**：{source_report}

---

## 一、核心财务摘要

_单位：人民币亿元；比率单位：% 或 ppt_

| 指标             |       {prior_year}年       |       {year}年       |        增速/变动         | 备注                      |
| ---------------- | :------------------------: | :------------------: | :----------------------: | ------------------------- |
| 营收             |      {prior_revenue}       |      {revenue}       |      {revenue_yoy}       | {revenue_note}            |
| 毛利             |         {prior_gp}         |         {gp}         |         {gp_yoy}         | {gp_note}                 |
| 毛利率           |        {prior_gpm}         |        {gpm}         |        {gpm_chg}         | {gpm_note}                |
| EBITDA           |       {prior_ebitda}       |       {ebitda}       |       {ebitda_yoy}       | {ebitda_note}             |
| EBITDA率         |   {prior_ebitda_margin}    |   {ebitda_margin}    |   {ebitda_margin_chg}    | {ebitda_margin_note}      |
| 归母净利润       |     {prior_net_profit}     |     {net_profit}     |     {net_profit_yoy}     | {net_profit_note}         |
| 扣非净利润       |    {prior_core_profit}     |    {core_profit}     |    {core_profit_yoy}     | {core_profit_note}        |
| 扣非净利率       | {prior_core_profit_margin} | {core_profit_margin} | {core_profit_margin_chg} | {core_profit_margin_note} |
| 经营性现金流净额 |        {prior_ocf}         |        {ocf}         |        {ocf_yoy}         | {ocf_note}                |
| 净现比           |  {prior_cash_conversion}   |  {cash_conversion}   |  {cash_conversion_chg}   | {cash_conversion_note}    |
| 销售费用         |    {prior_selling_exp}     |    {selling_exp}     |      {selling_yoy}       | {selling_note}            |
| 销售费用率       |    {prior_selling_rate}    |    {selling_rate}    |    {selling_rate_chg}    | {selling_rate_note}       |
| 管理费用         |     {prior_admin_exp}      |     {admin_exp}      |       {admin_yoy}        | {admin_note}              |
| 管理费用率       |     {prior_admin_rate}     |     {admin_rate}     |     {admin_rate_chg}     | {admin_rate_note}         |
| 研发费用         |       {prior_rd_exp}       |       {rd_exp}       |         {rd_yoy}         | {rd_note}                 |
| 研发费用率       |      {prior_rd_rate}       |      {rd_rate}       |      {rd_rate_chg}       | {rd_rate_note}            |
| 研发投入         |      {prior_rd_input}      |      {rd_input}      |      {rd_input_yoy}      | {rd_input_note}           |
| 资本化研发       |       {prior_cap_rd}       |       {cap_rd}       |       {cap_rd_yoy}       | {cap_rd_note}             |
| 资本化率         |      {prior_cap_rate}      |      {cap_rate}      |      {cap_rate_chg}      | {cap_rate_note}           |
| 固定资产折旧     |       {prior_fa_dep}       |       {fa_dep}       |       {fa_dep_yoy}       | {fa_dep_note}             |
| 固定资产折旧率   |    {prior_fa_dep_rate}     |    {fa_dep_rate}     |    {fa_dep_rate_chg}     | {fa_dep_rate_note}        |
| 固定资产期末余额 |     {prior_fa_balance}     |     {fa_balance}     |     {fa_balance_yoy}     | {fa_balance_note}         |
| 在手现金         |        {prior_cash}        |        {cash}        |        {cash_yoy}        | {cash_note}               |
| 附息债务         |        {prior_debt}        |        {debt}        |        {debt_yoy}        | {debt_note}               |
| 净现金/净债务    |      {prior_net_cash}      |      {net_cash}      |      {net_cash_chg}      | {net_cash_note}           |

> 注：对无法可靠计算的项目保留指标行并填写“无法有效计算”；如使用经调整净利润代理扣非净利润、或使用重构 EBITDA、或使用固定资产净额估算折旧率，必须在备注中写清口径。

## 二、关键证据摘录

| 主题                  | 原文/数字摘录          | 摘要结论               | 后续用途            |
| --------------------- | ---------------------- | ---------------------- | ------------------- |
| EBITDA 披露或重构依据 | {ebitda_evidence}      | {ebitda_takeaway}      | {ebitda_usage}      |
| 扣非净利润口径        | {core_profit_evidence} | {core_profit_takeaway} | {core_profit_usage} |
| 经营性现金流          | {ocf_evidence}         | {ocf_takeaway}         | {ocf_usage}         |
| 销售/管理/研发费用    | {opex_evidence}        | {opex_takeaway}        | {opex_usage}        |
| 研发投入与资本化      | {rd_cap_evidence}      | {rd_cap_takeaway}      | {rd_cap_usage}      |
| 开发支出滚动/摊销     | {dev_cost_evidence}    | {dev_cost_takeaway}    | {dev_cost_usage}    |
| 固定资产折旧与政策    | {dep_evidence}         | {dep_takeaway}         | {dep_usage}         |
| 所得税与有效税率      | {tax_evidence}         | {tax_takeaway}         | {tax_usage}         |
| 分部/主营业务拆分     | {segment_evidence}     | {segment_takeaway}     | {segment_usage}     |

## 三、口径与限制

| 项目                 | 结论                     |
| -------------------- | ------------------------ |
| EBITDA 口径          | {ebitda_basis}           |
| 扣非净利润口径       | {core_profit_basis}      |
| 资本化研发可见性     | {cap_visibility}         |
| 资本化摊销可见性     | {amort_visibility}       |
| 固定资产折旧率口径   | {dep_rate_basis}         |
| 经营性现金流可还原性 | {ocf_restoreability}     |
| 现金与债务可勾稽性   | {cash_debt_traceability} |
| 其他待跟进问题       | {open_questions}         |

## 四、摘要结论

1. **{conclusion_1_title}**：{conclusion_1_detail}
2. **{conclusion_2_title}**：{conclusion_2_detail}
3. **{conclusion_3_title}**：{conclusion_3_detail}

---

> **后续步骤**：优先基于本摘要文件继续生成 `{公司名}-{year}-还原.md`，再进入 `{公司名}-{year}-估值.md`。
