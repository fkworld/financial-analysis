# {公司名} {year}年估值分析

> **汇率假设**：{exchange_rate_note}
>
> **估值基准日**：{valuation_date}
>
> **估值模型**：{model_name}
>
> **股份代号**：{ticker}
>
> **数据来源**：{data_sources}

---

## 估值结论

|                        |            人民币 | {foreign_currency} |
| ---------------------- | ----------------: | -----------------: |
| **合理市值区间**       |  {mcap_range_rmb} |    {mcap_range_fc} |
| **每股目标价区间**     | {price_range_rmb} |   {price_range_fc} |
| **中枢估值（总市值）** |    {mcap_mid_rmb} |      {mcap_mid_fc} |
| **中枢目标价（每股）** |   {price_mid_rmb} |     {price_mid_fc} |

> 以下为详细分析过程。

---

## 一、关键参数

| 项目                  |                  数值 |
| --------------------- | --------------------: |
| 已发行股份            |  {shares_outstanding} |
| 全面摊薄股份          |      {diluted_shares} |
| 在手现金              |                {cash} |
| 附息债务              |                {debt} |
| **净现金/净债务**     |        **{net_cash}** |
| {year} 营收           |             {revenue} |
| {year} 毛利           |        {gross_profit} |
| {year} 毛利率         |                 {gpm} |
| {year} 净利润（报告） | {net_income_reported} |
| {year} 净利润（还原） | {net_income_adjusted} |
| {year} 核心业务量     |       {volume_metric} |
| 经营活动现金流        |                 {ocf} |
| 资本开支              |               {capex} |
| 自由现金流            |                 {fcf} |

## 二、{next_year} 年盈利预测

{guidance_note}

| 项目                   |                  保守 |                  基准 |                  乐观 |
| ---------------------- | --------------------: | --------------------: | --------------------: |
| 核心业务量             |            {vol_bear} |            {vol_base} |            {vol_bull} |
| **总营收（亿元）**     |        **{rev_bear}** |        **{rev_base}** |        **{rev_bull}** |
| **营收增速**           | **{rev_growth_bear}** | **{rev_growth_base}** | **{rev_growth_bull}** |
| 毛利率                 |            {gpm_bear} |            {gpm_base} |            {gpm_bull} |
| 毛利（亿元）           |             {gp_bear} |             {gp_base} |             {gp_bull} |
| 费用合计（亿元）       |           {opex_bear} |           {opex_base} |           {opex_bull} |
| **净利润（亿元）**     |         **{ni_bear}** |         **{ni_base}** |         **{ni_bull}** |
| **自由现金流（亿元）** |        **{fcf_bear}** |        **{fcf_base}** |        **{fcf_bull}** |

## 三、估值方法

### 方法一：远期 PE（核心净利润）

{pe_note}

| 情景 |  PE 倍数  | 核心净利润 | 总市值（人民币） |
| ---- | :-------: | ---------: | ---------------: |
| 保守 | {pe_bear} |  {ni_base} |   {mcap_pe_bear} |
| 基准 | {pe_base} |  {ni_base} |   {mcap_pe_base} |
| 乐观 | {pe_bull} |  {ni_base} |   {mcap_pe_bull} |

### 方法二：远期 PS（营收倍数）

{ps_note}

| 情景 |  PS 倍数  |       营收 | 总市值（人民币） |
| ---- | :-------: | ---------: | ---------------: |
| 保守 | {ps_bear} | {rev_base} |   {mcap_ps_bear} |
| 基准 | {ps_base} | {rev_base} |   {mcap_ps_base} |
| 乐观 | {ps_bull} | {rev_base} |   {mcap_ps_bull} |

### 方法三：EV/Sales（企业价值/营收）

{ev_sales_note}

| 情景 |    EV/Sales     |       营收 | 企业价值（人民币） |     净现金/净债务调整 |   股权价值（人民币） |
| ---- | :-------------: | ---------: | -----------------: | --------------------: | -------------------: |
| 保守 | {ev_sales_bear} | {rev_base} |          {ev_bear} | {net_cash_adjustment} | {mcap_ev_sales_bear} |
| 基准 | {ev_sales_base} | {rev_base} |          {ev_base} | {net_cash_adjustment} | {mcap_ev_sales_base} |
| 乐观 | {ev_sales_bull} | {rev_base} |          {ev_bull} | {net_cash_adjustment} | {mcap_ev_sales_bull} |

### 方法四：自由现金流收益率（FCF Yield）

{fcf_note}

| 情景 |    FCF Yield     | 自由现金流 | 总市值（人民币） |
| ---- | :--------------: | ---------: | ---------------: |
| 保守 | {fcf_yield_bear} | {fcf_base} |  {mcap_fcf_bear} |
| 基准 | {fcf_yield_base} | {fcf_base} |  {mcap_fcf_base} |
| 乐观 | {fcf_yield_bull} | {fcf_base} |  {mcap_fcf_bull} |

## 四、估值交叉验证

| 方法      |         保守（亿元） |         基准（亿元） |         乐观（亿元） | 适用性                   |
| --------- | -------------------: | -------------------: | -------------------: | ------------------------ |
| 远期 PE   |       {mcap_pe_bear} |       {mcap_pe_base} |       {mcap_pe_bull} | {pe_applicability}       |
| 远期 PS   |       {mcap_ps_bear} |       {mcap_ps_base} |       {mcap_ps_bull} | {ps_applicability}       |
| EV/Sales  | {mcap_ev_sales_bear} | {mcap_ev_sales_base} | {mcap_ev_sales_bull} | {ev_sales_applicability} |
| FCF Yield |      {mcap_fcf_bear} |      {mcap_fcf_base} |      {mcap_fcf_bull} | {fcf_applicability}      |

{valuation_conclusion_note}

## 五、还原数据对估值的影响

{restoration_impact_note}

## 六、主要风险

{risk_list}

---

> **免责声明**：本分析基于公开财报数据和合理假设，不构成投资建议。估值模型依赖对未来增长和利润率的预测，实际结果可能与预测存在重大差异。
