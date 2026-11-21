# Evidence and methods: sourced reference

Checked on 2026-10-02 against the primary sources listed. Quotes are verbatim. Items that could not be confirmed in a primary source are marked **unverified**. Use this file to cite methods and evidence; do not quote figures that are not in it.

Conventions used in this document:

- "Opened" means the page, PDF or source code was read directly, not a search snippet.
- When only a working-paper version was readable, the figures come from that version and this is stated.
- Code defaults come from the source code at the commit stated, not from documentation alone.

---

## 1. Methods for geo experiments

### 1.1 Geo-Based Regression (GBR)

- **Paper**: Jon Vaver, Jim Koehler (2011). "Measuring Ad Effectiveness Using Geo Experiments". Google Inc. technical report. https://research.google/pubs/measuring-ad-effectiveness-using-geo-experiments/
- **What it does**: geos are randomly assigned to control or treatment. Each geo's test-period response is regressed on its pretest response and its incremental ad spend.
- **Model, as stated**: "yi,1 = β0 + β1 yi,0 + β2 δi + ϵi", where δi is "the difference between the actual ad spend in geo i and the ad spend that would have occurred without the experiment". β2 is the return on ad spend.
- **Weights**: "This model is fit using weights wi = 1/yi,0 in order to control for heteroscedasticity caused by the differences in geo size."
- **Design aid**: the paper predicts confidence-interval width from pretest data, using pseudo pretest and test periods. It reports that constrained randomization (rank geos by pretest volume, assign one per pair) gives confidence intervals "lower by about 10%".
- **Assumptions**: randomization of geos; a linear relationship between pretest and test response; enough geos to estimate the regression.
- **When it fails**: Kerman et al. (2017) state that GBR "draws its statistical power from the number of available geos in the analysis, and therefore is not applicable for situations with only a few geos available (such as matched market tests)."

### 1.2 Time-Based Regression (TBR)

- **Paper**: Jouni Kerman, Peng Wang, Jon Vaver (2017). "Estimating Ad Effectiveness using Geo Experiments in a Time-Based Regression Framework". Google Inc. technical report. https://research.google/pubs/estimating-ad-effectiveness-using-geo-experiments-in-a-time-based-regression-framework/
- **What it does**: aggregates treatment and control geos into two time series. A regression fitted on the pretest predicts the treatment counterfactual during the test. The cumulative difference is the causal effect.
- **Model, as stated**: "yt = α + βxt + ϵt, t in pretest period", where yt and xt are the treatment and control series.
- **Periods**: "A geo experiment consists of several, distinct time periods: the pretest, intervention, and cooldown periods." The cooldown captures lagged effects.
- **Worked example**: "a pretest period of eight weeks and a cooldown period of one week."
- **Assumptions, as stated**: "This model assumes that the control time series acts as a sufficient predictor for the behavior of the treatment time series across the pretest, intervention, and cooldown periods." The relationship "is therefore assumed to be stable".
- **When it fails**: when the treatment and control relationship drifts between pretest and test (non-stationary residuals). The paper also notes that an unnecessary cooldown "only adds more uncertainty to the estimate of iROAS."

### 1.3 Matched markets design (Au 2018)

- **Paper**: Tim Au (2018). "A Time-Based Regression Matched Markets Approach for Designing Geo Experiments". Google LLC technical report. https://research.google/pubs/a-time-based-regression-matched-markets-approach-for-designing-geo-experiments/ (PDF: https://storage.googleapis.com/gweb-research2023-media/pubtools/5500.pdf)
- **What it does**: replaces randomization with a greedy search for treatment and control groups whose time series best satisfy the TBR assumptions, subject to advertiser constraints.
- **When to use**: few geos, unbalanced populations, or geos forced into a group.
- **When it fails**: the design gives up randomization. Validity rests on the TBR model fitting and predicting well. The Meridian GeoX FAQ adds that TBRMM "estimates design power based on the pre-test in-sample fit", and that "the pre-test variance could often be underestimated compared to what is experienced during the actual test."
- **Code**: https://github.com/google/matched_markets

### 1.4 Trimmed Match

- **Paper**: Aiyou Chen, Tim Au (2022). "Robust Causal Inference for Incremental Return on Ad Spend with Randomized Paired Geo Experiments". Annals of Applied Statistics 16(1). DOI 10.1214/21-AOAS1493. arXiv: https://arxiv.org/abs/1908.02922
- **What it does**: geos are paired, and one geo per pair is randomized to treatment. The iROAS estimate solves for θ where the trimmed mean of pair-level residuals (response difference minus θ times spend difference) is zero. The trim rate is chosen from the data.
- **Framing, as stated**: "only a small number of highly heterogeneous units are used". The estimator is described as "robust, distribution-free and interpretable".
- **Design companion**: Aiyou Chen, Marco Longfils, Nicolas Remy (2021). "Trimmed Match Design for Randomized Paired Geo Experiments". arXiv:2105.07060. https://arxiv.org/abs/2105.07060
- **Assumptions**: randomized pairs; the paper builds on instrumental-variable reasoning and allows interference from budget constraints.
- **When it fails**: trimming discards information from extreme pairs, so it needs enough pairs to trim. The paper investigates "sensitivity of Trimmed Match to some violations of its assumptions". The library README marks the code "For research purposes only".
- **Code**: https://github.com/google/trimmed_match

### 1.5 Synthetic control

- **Paper**: Alberto Abadie, Alexis Diamond, Jens Hainmueller (2010). "Synthetic Control Methods for Comparative Case Studies: Estimating the Effect of California's Tobacco Control Program". Journal of the American Statistical Association 105(490): 493-505. DOI 10.1198/jasa.2009.ap08746
- **What it does**: builds a weighted average of untreated units (non-negative weights summing to one) that tracks the treated unit before the intervention. The post-period gap is the effect.
- **Guidance paper**: Alberto Abadie (2021). "Using Synthetic Controls: Feasibility, Data Requirements, and Methodological Aspects". Journal of Economic Literature 59(2): 391-425. https://www.aeaweb.org/articles?id=10.1257/jel.20191450
- **Contextual requirements listed by Abadie (2021)**: availability of a comparison group, no anticipation, no interference, the convex hull condition, and a sufficient time horizon.
- **When it fails, quoted from Abadie (2021)**:
  - Poor fit: "a large T0 cannot drive down the bias if the fit is bad."
  - Volatility: "the impact of 'small' interventions with effects of a magnitude similar to the volatility of the outcome are difficult to detect."
  - Donor pool: "Including in the donor pool units that are regarded by the analyst to be unsuitable controls ... is a recipe for bias."
  - Spillover: "if spillover effects are substantial and affect units in close geographical proximity, those units may provide a biased estimate of the counterfactual".
  - Credibility: it "depends on its ability to track the trajectory of the outcome variable for the treated unit for an extended pre-intervention period."

### 1.6 Augmented synthetic control (ASCM)

- **Paper**: Eli Ben-Michael, Avi Feller, Jesse Rothstein (2021). "The Augmented Synthetic Control Method". Journal of the American Statistical Association 116(536): 1789-1803. DOI 10.1080/01621459.2021.1929245. arXiv: https://arxiv.org/abs/1811.04170
- **What it does**: "uses an outcome model to estimate the bias due to imperfect pre-treatment fit and then de-biases the original SCM estimate." The main proposal uses ridge regression as the outcome model.
- **Assumptions**: the outcome model is approximately correct. The paper gives error bounds under linear factor models.
- **Trade-off**: the reformulated estimator allows negative weights on some donors. This means extrapolation outside the convex hull, which the ridge penalty limits.
- **Code**: augsynth R package.

### 1.7 Synthetic difference-in-differences (SDID)

- **Paper**: Dmitry Arkhangelsky, Susan Athey, David A. Hirshberg, Guido W. Imbens, Stefan Wager (2021). "Synthetic Difference-in-Differences". American Economic Review 111(12): 4088-4118. https://www.aeaweb.org/articles?id=10.1257/aer.20190159 (arXiv: https://arxiv.org/abs/1812.09970)
- **What it does**: a weighted two-way fixed effects regression using both unit weights and time weights.
- **Weights, quoted**: "Unit weights are designed so that the average outcome for the treated units is approximately parallel to the weighted average for control units." "Time weights are designed so that the average post-treatment outcome for each of the control units differs by a constant from the weighted average of the pre-treatment outcomes".
- **Inference**: the paper gives bootstrap, jackknife and placebo variance estimators. The placebo variant can be applied with a single treated unit.
- **Assumptions**: outcomes follow a latent factor structure with unit and time factors.

### 1.8 Conformal inference for synthetic control

- **Paper**: Victor Chernozhukov, Kaspar Wüthrich, Yinchu Zhu (2021). "An Exact and Robust Conformal Inference Method for Counterfactual and Synthetic Controls". Journal of the American Statistical Association 116(536): 1849-1864. DOI 10.1080/01621459.2021.1920957. arXiv: https://arxiv.org/abs/1712.09089
- **What it does**: treats inference as counterfactual prediction plus a structural-break test. It permutes residuals under the null to build p-values and confidence sets. It works with SC, DiD, factor and matrix completion models.
- **Assumptions, quoted**: validity holds if "the stochastic shock sequence {ut} is stationary and weakly dependent" and the estimator is consistent, or under misspecification if the data "are stationary and weakly dependent" and the estimator is stable. "Estimation under the null guarantees the exact finite sample validity of our procedures if the data are iid or exchangeable."
- **When it fails**: non-stationary shocks, or a shock distribution changed by something other than the intervention.

### 1.9 CausalImpact (Bayesian structural time series)

- **Paper**: Kay H. Brodersen, Fabian Gallusser, Jim Koehler, Nicolas Remy, Steven L. Scott (2015). "Inferring causal impact using Bayesian structural-time-series models". Annals of Applied Statistics 9(1): 247-274. DOI 10.1214/14-AOAS788. https://research.google/pubs/inferring-causal-impact-using-bayesian-structural-time-series-models/
- **What it does**: "a diffusion-regression state-space model that predicts the counterfactual market response that would have occurred had no intervention taken place."
- **Assumptions, from the package documentation** (https://google.github.io/CausalImpact/CausalImpact.html):
  - Control series "were themselves not affected by the intervention."
  - "the relationship between covariates and treated time series, as established during the pre-period, remains stable throughout the post-period."
  - Results are sensitive to priors, in particular `prior.level.sd`.
- **When it fails**: contaminated controls (spillover), structural breaks in the covariate relationship, or priors that do not fit the data.

### 1.10 Meta GeoLift (open-source R package)

Source: repository https://github.com/facebookincubator/GeoLift, cloned at commit db34ea4 (2026-04-01), `DESCRIPTION` Version 2.7.5. Documentation: https://facebookincubator.github.io/GeoLift/

- **Method, as stated in `Methodology.md`**: "GeoLift uses ASCM to estimate and de-bias the synthetic control estimate and then uses GSC's robustness on small samples and on heterogeneous effects across units to perform inference."
- **Confidence intervals**: default is conformal inference (Chernozhukov, Wüthrich, Zhu). When it fails, GeoLift falls back to "jackknife+".
- **Market selection**: `GeoLiftMarketSelection` "provides a ranking of test markets for a GeoLift test based on a power analysis." Candidates come from a similarity ranking (correlations by default; `dtw = 0`). Power is simulated by injecting effect sizes into historical periods (`lookback_window`).
- **Ranking criteria (docs)**: "EffectSize, Power, AvgScaledL2Imbalance, Average_MDE, and abs_lift_in_zero".
- **Defaults in `GeoLiftMarketSelection` code**:
  - `effect_size = seq(-0.2, 0.2, 0.05)`. The function's docstring states `seq(0,0.25,0.05)`, so docs and code disagree.
  - `lookback_window = 1`, `cpic = 1`, `alpha = 0.1`, `model = "none"`, `fixed_effects = TRUE`, `dtw = 0`.
  - `side_of_test = "two_sided"`, `conformal_type = "iid"`, `ns = 1000`, `run_stochastic_process = FALSE`.
- **Defaults in `GeoLiftPower`**: `effect_size = seq(0, 1, 0.05)`, `cpic = 0`, `alpha = 0.1`, `ns = 1000`.
- **Model option guidance (docstring)**: "Ridge" is "Recommended to improve fit for smaller panels (less than 40 locations and 100 time-stamps.)". "GSYN" is recommended for larger panels.
- **Best practices (`BestPractices.md`)**:
  - "Daily granularity in the data is strongly recommended over weekly."
  - "We recommend having at least 4 - 5x the test duration of pre-campaign historical data of stable data".
  - "At minimum we recommend having 25 pre-treatment periods of 20 or more geo-units."
  - "Study should be run for a minimum of 15 days, if daily, and a minimum of 4-6 weeks if weekly".
  - "The test duration should cover at least one purchase cycle for the product."
- **Spillover tool**: GeoLift documents use of Meta's Commuting Zones as geo units "to take the commuter effect into account for the geographical randomisation."

### 1.11 Google Meridian GeoX

Sources: repository https://github.com/google/meridian-geox (cloned 2026-10-02, head 3424ae0); documentation https://developers.google.com/meridian/geox; paper page https://research.google/pubs/meridian-geox-an-open-source-framework-for-precision-and-efficiency-in-geo-experiments/

- **Paper**: Steven Ye, Fabian Sinn, Yunxiao Li, Yang Jiao (2026). "Meridian GeoX: An Open-Source Framework for Precision and Efficiency in Geo Experiments". Google.
- **Release history (git)**: initial import 2026-04-15; tags 0.1.0rc2 (2026-08-11), v0.1.1 (2026-08-31), v1.0.0 (2026-09-01), v1.0.1 (2026-09-02). License Apache-2.0.
- **Public announcement date**: **unverified**. The business.google.com announcement page redirected to a consent wall and could not be read.

**Methods: paper versus code**

- The paper abstract lists "data-driven stratified sampling, advanced counterfactual models" (TBR, Synthetic Control, SDID) and a "Design-Aware Placebo Inference engine".
- The released code implements **TBR only**. The `Methodology` enum has `TBR = 1` and `SDID = 2`, but `analysis.py` raises "Unsupported methodology ... Only TBR is supported." Synthetic Control does not appear in the code. The FAQ states: "GeoX supports the time-based regression (TBR) methodology."
- **TBR as implemented (docs)**: fits "Ȳtreat,t = α + β Ȳcontrol,t + εt" on group averages by OLS, with "a non-negativity constraint: β ≥ 0". "No distributional assumptions are made on εt, and uncertainty is quantified using non-parametric placebo-based inference."

**Design**

- Experiment types: HOLDBACK (default), GO_DARK, HEAVY_UP, with native multi-cell against a common control.
- **Stratified sampling (docs)**: KPI series are featurized by "the mean, coefficient of variation (CV), slope, autocorrelation (at lag 1), and dynamic time warping (DTW)". "The default number of clusters is four." Randomization happens within each cluster.
- **Random sampling (docs)**: "not generally recommended over the stratified sampling methodology, however, it becomes necessary in GeoX with a small number of geos."
- **Design search**: splits the pretest into training, validation and selection periods. Candidates are scored on out-of-sample R², A/A robustness, MDE and budget.
- **MDE formula (docs)**: "MDE_lift = Min incremental conversion / Baseline control conversion = SE_lift × (Z_{1-α/2} + Z_{1-β}) / Baseline control conversion".

**Inference: design-aware placebo**

- Standard placebo tests shuffle labels across all control-geo splits, which "frequently generates 'bad splits'". This "doesn't just inflate the type-I error rate, it also makes detecting a true incremental lift more difficult."
- Design-aware inference draws placebo assignments from the same constrained design space: "Placebos are generated using the identical objective functions, budget limits, and design constraints."
- In code, `analyze()` requires the `Design` object and regenerates placebos under its `geo_assignment_rule` (RANDOM or STRATIFIED_SAMPLING). A hand-picked test cell has no generating rule to replay.

**Code defaults (`api.py`)**

| Parameter | Default |
|---|---|
| `alpha` | 0.1 |
| `power` | 0.8 |
| `test_type` | TWO_SIDED |
| `geo_assignment_rule` | STRATIFIED_SAMPLING |
| `num_strata` | 4 |
| `min_r2` (design candidates) | 0.8 |
| `n_candidates` | 100,000 |
| `max_conversions_percent` (treatment share) | 0.3 |
| `n_placebo_candidates` | 100,000 |
| `n_top_placebos` | 500 |
| `min_placebo_r2` | 0.6 |
| `min_placebo_count_warning` | 100 |
| `min_placebo_count_error` | 10 |

**Data and practice guidance (docs)**

- Daily data only: "GeoX strictly requires daily time-series data. Weekly data isn't supported".
- Pretest: "a minimum of 3*N days worth of response data ... where N is equals to the duration of the actual test period". Use a year or more under strong seasonality.
- Geo count: "You should include a minimum of 10 geos for a single-cell design." Random sampling for 10-20 geos, stratified for more than 20. "ranging from 50 to more than 100" geos is recommended.
- Timeline: "About 7–14 weeks is typically needed from pretest planning to completion of actual analysis." Active test "3–10 weeks". Cooldown "2+ weeks" on the implementation page; the FAQ says "maintain a 1-2 week cooldown period".
- Multi-cell: "Results for each treatment cell are evaluated independently against the shared control." There is no direct test of the difference between two treatment arms.

---

## 2. Evidence for practitioners

### 2.1 Blake, Nosko, Tadelis (2015), eBay paid search

- **Citation**: Thomas Blake, Chris Nosko, Steven Tadelis (2015). "Consumer Heterogeneity and Paid Search Effectiveness: A Large-Scale Field Experiment". Econometrica 83(1): 155-174. DOI 10.3982/ECTA12423
- **Version read**: NBER WP 20171 (May 2014) and the accepted version "Forthcoming in Econometrica" (August 12, 2014). Figures below match in both.
- **Brand keywords**: eBay halted brand-term ads on Yahoo! and MSN. "almost all (99.5 percent) of the forgone click traffic from turning off brand keyword paid search was immediately captured by natural search traffic". The abstract: "brand-keyword ads have no measurable short-term benefits."
- **Non-brand keywords**: ads were suspended "in roughly 30 percent of DMAs", chosen to "minimize the potential cost and impact to the business".
- **Bias of observational ROI**: OLS gives "a ROI of over 4,100% without time and geographic controls, and a ROI of over 1,400% with such controls." The experiment gives "a ROI of −63%, with a 95% confidence interval of [−124%,−3%]".
- **Heterogeneity**: "new and infrequent users are positively influenced by ads but ... more frequent users whose purchasing behavior is not influenced by ads account for most of the advertising expenses".

### 2.2 Simonov, Nosko, Rao (2018), competitive brand search

- **Citation**: Andrey Simonov, Chris Nosko, Justin M. Rao (2018). "Competition and Crowd-Out for Brand Keywords in Sponsored Search". Marketing Science 37(2): 200-215. DOI 10.1287/mksc.2017.1065
- **Setting**: "large-scale experiments on Bing with data from thousands of brands."
- **No competitors**: "a positive, statistically significant impact of brand ads of 1%–4%, with larger brands having a smaller causal effect."
- **Competitors present, focal ad shown**: "competitors in paid positions 2–4 can 'steal' 1%–5% of the focal brand's clicks".
- **Competitors present, focal brand not advertising**: "competitors 'steal' 18%–42% of clicks".
- **Conclusion**: "the return on investment on defensive advertising to be strongly positive."
- **Implication for brand-search blackouts**: the result of a brand blackout depends on whether competitors bid on the brand term during the test.

### 2.3 Lewis and Rao (2015), the power problem

- **Citation**: Randall A. Lewis, Justin M. Rao (2015). "The Unfavorable Economics of Measuring the Returns to Advertising". Quarterly Journal of Economics 130(4): 1941-1973. DOI 10.1093/qje/qjv023
- **Data**: "Twenty-five large field experiments ... collectively representing $2.8 million in digital advertising expenditure".
- **Key numbers, quoted**:
  - "The median confidence interval on return on investment is over 100 percentage points wide."
  - "a coefficient of variation of 10 is common."
  - "informative advertising experiments can easily require more than 10 million person-weeks".
  - "the median standard error on ROI for the retail experiments is 26.1%". "The median standard error for the brokerages was 115%."
  - The median campaign "had to causally raise average per person sales by $0.35", against "a mean of $7 and a standard deviation of $75". "the R² for a highly profitable campaign would be on the order of 0.0000054."

### 2.4 Gordon, Zettelmeyer, Bhargava, Chapsky (2019), observational methods vs RCTs

- **Citation**: Brett R. Gordon, Florian Zettelmeyer, Neha Bhargava, Dan Chapsky (2019). "A Comparison of Approaches to Advertising Measurement: Evidence from Big Field Experiments at Facebook". Marketing Science 38(2): 193-225. DOI 10.1287/mksc.2018.1135
- **Version read**: MSI Working Paper 18-113. The journal abstract (Crossref) reads only: "Observational methods often fail to accurately recover the treatment effects generated from randomized advertising experiments on Facebook."
- **Data**: "15 U.S. advertising experiments at Facebook comprising 500 million user-experiment observations and 1.6 billion ad impressions".
- **Results, quoted from the working paper**:
  - "Generally, the observational methods overestimate ad effectiveness relative to the RCT, although in some cases, they significantly underestimate effectiveness."
  - "in half of our studies, the estimated percentage increase in purchase outcomes is off by a factor of three across all methods."
  - "the point estimates in seven of the 14 studies with a checkout-conversion outcome are consistently off by more than a factor of three."

### 2.5 Johnson, Lewis, Nubbemeyer (2017), ghost ads

- **Citation**: Garrett A. Johnson, Randall A. Lewis, Elmar I. Nubbemeyer (2017). "Ghost Ads: Improving the Economics of Measuring Online Ad Effectiveness". Journal of Marketing Research 54(6): 867-884. DOI 10.1509/jmr.15.0297
- **Method**: ghost ads log when the experimental ad would have been served to a control-group user. This identifies the control counterparts of exposed users without PSA ads.
- **Results, journal abstract (via Crossref)**:
  - "their implementation records more than 100 million predicted ghost ads per day."
  - "the ads lifted website visits by 17.2% and purchases by 10.5%."
  - "advertisers can measure ad lift just as precisely while spending at least an order of magnitude less."
- **Note**: earlier working-paper versions report different rounding (17% and 11%). Use the journal figures.

### 2.6 Carryover after a campaign ends

- **Source**: Garrett Johnson, Randall A. Lewis, Elmar Nubbemeyer (2015). "The Online Display Ad Effectiveness Funnel & Carryover: Lessons from 432 Field Experiments". SSRN working paper, DOI 10.2139/ssrn.2701578. Journal publication: **unverified**.
- **Results, quoted from the abstract**:
  - "432 online display ad field experiments on the Google Display Network" across "431 advertisers".
  - "median lifts of 17% and 8%" for site visits and conversions.
  - "most campaigns have a modest, positive carryover four weeks after the campaign ended with a further 6% lift in visitors and 16% lift in visits on average, relative to the in-campaign lift."
  - "a 10% lift in site visitors translates into a 5-7% lift in converters."
- **Vaver and Koehler (2011)**: "Incremental sales continue to be generated even after the ad spend returns to pretest levels in all geos."

### 2.7 Test duration

- **Google Conversion Lift (users)**: "We allow studies as short as 7 days but typically recommend more than 14 days." "We've found up to a 17% drop in Absolute Lift in studies with a long conversion lag that run for less than 14 days." Source: https://support.google.com/google-ads/answer/12005564
- **GeoLift**: minimum 15 days with daily data, 4-6 weeks with weekly data, at least one purchase cycle.
- **Meridian GeoX**: active test 3-10 weeks. Automated bidding may need extra time "to account for campaign learning period."

### 2.8 Spillover between geos

- **Source**: David Rolnick, Kevin Aydin, Jean Pouget-Abadie, Shahab Kamali, Vahab Mirrokni, Amir Najmi (2019). "Randomized Experimental Design via Geographic Clustering". KDD 2019, pp. 2745-2753. DOI 10.1145/3292500.3330778. arXiv: https://arxiv.org/abs/1611.03780
- **Finding**: "users may issue queries from multiple geographical locations, geo-regions cannot be considered independent and interference may be present in the experiment." GeoCUTS builds clusters from Google Search user movement to reduce interference. It "performs comparably to DMAs".
- **Meridian GeoX docs**: smaller geo units add power, but "people may naturally travel across geo regions, causing contamination bias effect to the incrementality metric."
- **Abadie (2021)**: spillover can be handled by removing affected units from the donor pool, at the cost of match quality.

---

## 3. Platform tools as of 2026

### 3.1 Google Ads Conversion Lift

**Lower spend threshold**

- Google announcement dated **November 11, 2025**: "What once might have cost upwards of $100,000 for a single experiment can now be done for $5,000." It also claims conclusive results "up to 50% more frequently". Source: https://support.google.com/google-ads/answer/16719772
- The announcement does not say whether the $5,000 applies to user-based, geo-based or both.
- Secondary sources date the $5K figure differently: PPC Land ties it to Google Marketing Live, May 22, 2025, and to November 11, 2025 in a second article. The Google page above carries November 11, 2025.

**Conversion Lift based on users** (https://support.google.com/google-ads/answer/12005564)

- "You must have at least 1,000 observed conversions."
- "The study requires a minimum campaign budget of $5,000 USD."
- Supported: "Display, Search, Video, Demand Gen, App Campaigns and Performance Max campaigns". iOS-targeted App campaigns and Travel Ads are not supported.
- Holdback "from 1% to 50%". With Brand Lift and Search Lift running, "you must leave the 30% holdback."
- Certainty shown "from 50% to 95%, in 5% increments". "Aim for 90% certainty". Results "between 50% and 90% can be used as directional results."
- Access: "Conversion Lift isn't available for all Google Ads accounts. To use Conversion Lift, contact your Google account representative."

**Conversion Lift based on geography** (https://support.google.com/google-ads/answer/14097193 and https://support.google.com/google-ads/answer/14097991)

- Campaigns "must target a single country to be eligible for the geo-split methodology".
- Supported: "App, Demand Gen, Discovery, Display, Video, Search, Shopping, and Performance Max".
- Supports offline conversions at ZIP or city level.
- Budget: "budget requirement tends to be higher than users-based studies". A specific geo-based minimum is **unverified**.

**API access**

- Google Ads API v25.1 (release notes dated 2026-08-19) added read-only `LiftMeasurementConfig` ("a lift study"), `LiftMeasurementFlight`, Brand Lift dimension resources, and "24 new Conversion Lift metrics and winner score metrics". Source: https://developers.google.com/google-ads/api/docs/release-notes
- The resources are read-only. No create or mutate service for lift studies appears in the release notes.
- Allowlist-only access is reported by PPC Land (August 20, 2026). It does not appear in the Google release notes that were read. Status: **unverified in primary source**.

### 3.2 Meta Conversion Lift and Brand Lift

**Brand Lift minimums** (https://www.facebook.com/business/help/417527072254206)

- "These are minimums as of September 15, 2026."
- Selected countries: United States $175,000; United Kingdom $64,000; Germany $110,000; France $79,000; Spain $39,000; Italy $55,000; Canada $54,000; Australia $80,000; Brazil $58,000; Mexico $44,000; India $44,000.
- "The default minimum for countries not listed here is $15,000."
- With multiple target countries, "the system will leverage the country with the highest spend requirement."

**Brand Lift usage** (https://www.facebook.com/business/help/1693381447650068)

- "You shouldn't use Brand Lift if you have other active campaigns for the same brand or product running across Meta technologies."

**Conversion Lift**

- Conversion Lift on standard web events since October 1, 2021 requires Conversions API (https://www.facebook.com/business/help/453968412201452).
- Minimums: Meta says "some Conversion Lift and Brand Lift tests may display spend minimums or recommended spend amounts when you start creating your test" (https://www.facebook.com/business/help/2420136524735942). Account representatives set "what minimums or other requirements may apply".
- Third-party figures such as "$5,000 in the past year" and "500 optimized conversions" were found only on vendor blogs. Status: **unverified**.

**Confidence thresholds** (https://www.facebook.com/business/help/239549606692303)

- "We typically suggest tests have an estimated power of 80 percent or higher".
- "For lift tests, a 90 percent or higher confidence percentage represents a statistically reliable result. For A/B tests, a 65 percent or higher confidence percentage represents a winning result."

**API and AI connectors**

- Marketing API `ad_study` objects can be read. The `type` field includes LIFT, SPLIT_TEST, CONTINUOUS_LIFT_CONFIG and GEO_LIFT, with `cells` and `objectives` edges. Source: https://developers.facebook.com/docs/marketing-api/reference/ad-study
- Meta's Ads MCP server documentation lists "A/B tests and conversion lift studies" as a tool category: "Create and manage A/B tests and conversion lift studies, and retrieve details on existing tests and studies." Source: https://developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/ads-mcp-server-overview
- The server is hosted at `mcp.facebook.com/ads` according to secondary sources.
- Launch date April 29, 2026 and "open beta" status come from secondary sources only. Status: **unverified**.

---

## 4. Practical design rules with sources

### 4.1 Minimum number of geos

| Source | Rule |
|---|---|
| Meridian GeoX FAQ | "a minimum of 10 geos for a single-cell design"; random sampling for 10-20; stratified above 20; 50 to 100+ recommended |
| GeoLift Best Practices | "25 pre-treatment periods of 20 or more geo-units" |
| Kerman et al. 2017 | GBR "is not applicable for situations with only a few geos"; TBR and matched markets cover that case |
| Chen and Au 2022 | Trimmed Match targets "a small number of highly heterogeneous units" in randomized pairs |

Multi-cell designs "require significantly more geos and budget to maintain statistical power" (GeoX, types of experiments page).

### 4.2 Pre-period length relative to test length

| Source | Rule |
|---|---|
| GeoLift | "at least 4 - 5x the test duration" of stable pre-campaign data; 52 weeks preferred for seasonality |
| Meridian GeoX | "a minimum of 3*N days", N = test length in days; one year or more with strong seasonality |
| Kerman et al. 2017 | worked example with an 8-week pretest |
| Abadie 2021 | credibility depends on tracking the treated unit "for an extended pre-intervention period" |

### 4.3 Cooldown and buffer periods

- TBR defines a cooldown in which "ad campaigns are reset to their original state" so lagged effects are captured. Choose its end where cumulative iROAS stabilizes.
- GeoX: cooldown "highly recommended if the incremental effect of your campaigns could be delayed". During cooldown "all geos ... should stay at existing BAU".
- GeoX FAQ: "maintain a 1-2 week cooldown period". GeoX implementation page: "Cool-down and analysis (2+ weeks)".
- Warm-up: GeoX notes "The first few weeks of the test period might be reserved for your campaign warm-up".
- Evidence for lag length: carryover four weeks after display campaigns (Johnson, Lewis, Nubbemeyer 2015).

### 4.4 Backend KPIs instead of platform-attributed conversions

- GeoX: "you should use raw, unfiltered conversion time series instead of attributed conversions. This prevents the results from being skewed by predefined attribution logic".
- GeoX: "you shouldn't use attributed conversion events, as the choice of attribution model may bias the causal estimate".
- GeoX data: conversions are "typically from the advertiser's CRM". Use non-negative metrics (gross, not net of refunds).
- Evidence that attribution misleads: Blake et al. show OLS ROI over 1,400% against an experimental −63%. Gordon et al. find observational estimates "off by a factor of three" in half of studies.

### 4.5 Google Ads geo targeting: "Presence" vs "Presence or interest"

- Google Ads Help (https://support.google.com/google-ads/answer/1722038): "By default, location targeting includes both physical locations and locations of interest".
- Presence or interest: "Reach people in, regularly in, or who've shown interest in your targeted locations". Presence: "Reach people in or regularly in your targeted locations".
- GeoX implementation guide: "Avoid the default settings and 'Presence or Interest,' as interest-based targeting will serve ad impressions to users outside your preferred geo boundaries".
- GeoX also recommends positive geo targeting over national targeting with negative exclusions.
- Caveat: Google's "Presence" definition includes people "regularly in" a location, so it is not strictly physical location at impression time. This is a reading of the definition, not a Google statement about experiments.
- Budget leakage: for capped budgets, GeoX says duplicating the campaign is "Mandatory", because restricting geos "will cause the algorithm to spend the saved budget in the remaining control geos".
- Concurrent studies: "All user-level measurement studies such as conversion lift and brand lift should be deactivated on the campaigns under evaluation".

### 4.6 Holdout cost estimation

- Blake et al. limited the non-brand test to about 30% of DMAs "to reduce the scope of the test and minimize the potential cost".
- GeoX caps treatment size by default at `max_conversions_percent = 0.3` of conversions. It converts power into budget using spend history (go-dark, heavy-up) or a cost per incremental conversion (holdback).
- GeoLift sizes budgets from `cpic` (cost per incremental conversion) and a `budget` cap.
- Rule of thumb (derived here, not from a single source): expected cost of a go-dark test ≈ share of baseline KPI in treatment geos × expected incremental KPI per period × test length × value per unit, minus media saved. A heavy-up test costs the added spend times (1 − iROAS) when iROAS is below break-even.

### 4.7 Multiple testing

- Benjamini and Hochberg (1995) introduced the false discovery rate and a step-up procedure to control it. Journal of the Royal Statistical Society Series B 57(1): 289-300. DOI 10.1111/j.2517-6161.1995.tb02031.x
- Meridian GeoX evaluates each multi-cell arm "independently against the shared control". No multiplicity correction appears in the docs read, so an adjustment across cells or KPIs is left to the analyst.
- GeoX supports one primary KPI per study. Secondary KPIs may be underpowered, per the FAQ.
- GeoX design-aware inference targets type-I error control for a single test. It does not address multiple comparisons.

---

## 5. Items not verified

- Meridian GeoX public announcement date (Google Marketing Live preview on 5 May 2026 is not confirmed).
- Specific minimum budget for Google Conversion Lift based on geography.
- Allowlist requirement for Google Ads API lift resources.
- Numeric minimums for Meta Conversion Lift.
- Launch date and beta status of Meta Ads AI connectors.
- Journal publication of Johnson, Lewis, Nubbemeyer (432 experiments).

---

## References

1. Vaver, J., Koehler, J. (2011). Measuring Ad Effectiveness Using Geo Experiments. Google Inc. https://research.google/pubs/measuring-ad-effectiveness-using-geo-experiments/
2. Kerman, J., Wang, P., Vaver, J. (2017). Estimating Ad Effectiveness using Geo Experiments in a Time-Based Regression Framework. Google Inc. https://research.google/pubs/estimating-ad-effectiveness-using-geo-experiments-in-a-time-based-regression-framework/
3. Au, T. (2018). A Time-Based Regression Matched Markets Approach for Designing Geo Experiments. Google LLC. https://research.google/pubs/a-time-based-regression-matched-markets-approach-for-designing-geo-experiments/
4. Chen, A., Au, T. (2022). Robust Causal Inference for Incremental Return on Ad Spend with Randomized Paired Geo Experiments. Annals of Applied Statistics 16(1). https://doi.org/10.1214/21-AOAS1493 (arXiv: https://arxiv.org/abs/1908.02922)
5. Chen, A., Longfils, M., Remy, N. (2021). Trimmed Match Design for Randomized Paired Geo Experiments. arXiv:2105.07060. https://arxiv.org/abs/2105.07060
6. Abadie, A., Diamond, A., Hainmueller, J. (2010). Synthetic Control Methods for Comparative Case Studies: Estimating the Effect of California's Tobacco Control Program. Journal of the American Statistical Association 105(490): 493-505. https://doi.org/10.1198/jasa.2009.ap08746
7. Abadie, A. (2021). Using Synthetic Controls: Feasibility, Data Requirements, and Methodological Aspects. Journal of Economic Literature 59(2): 391-425. https://www.aeaweb.org/articles?id=10.1257/jel.20191450
8. Ben-Michael, E., Feller, A., Rothstein, J. (2021). The Augmented Synthetic Control Method. Journal of the American Statistical Association 116(536): 1789-1803. https://doi.org/10.1080/01621459.2021.1929245
9. Arkhangelsky, D., Athey, S., Hirshberg, D. A., Imbens, G. W., Wager, S. (2021). Synthetic Difference-in-Differences. American Economic Review 111(12): 4088-4118. https://www.aeaweb.org/articles?id=10.1257/aer.20190159
10. Chernozhukov, V., Wüthrich, K., Zhu, Y. (2021). An Exact and Robust Conformal Inference Method for Counterfactual and Synthetic Controls. Journal of the American Statistical Association 116(536): 1849-1864. https://doi.org/10.1080/01621459.2021.1920957
11. Brodersen, K. H., Gallusser, F., Koehler, J., Remy, N., Scott, S. L. (2015). Inferring causal impact using Bayesian structural-time-series models. Annals of Applied Statistics 9(1): 247-274. https://doi.org/10.1214/14-AOAS788
12. Meta Open Source. GeoLift R package, version 2.7.5. https://github.com/facebookincubator/GeoLift ; docs https://facebookincubator.github.io/GeoLift/
13. Ye, S., Sinn, F., Li, Y., Jiao, Y. (2026). Meridian GeoX: An Open-Source Framework for Precision and Efficiency in Geo Experiments. Google. https://research.google/pubs/meridian-geox-an-open-source-framework-for-precision-and-efficiency-in-geo-experiments/
14. Google. Meridian GeoX library, v1.0.1. https://github.com/google/meridian-geox ; docs https://developers.google.com/meridian/geox
15. Blake, T., Nosko, C., Tadelis, S. (2015). Consumer Heterogeneity and Paid Search Effectiveness: A Large-Scale Field Experiment. Econometrica 83(1): 155-174. https://doi.org/10.3982/ECTA12423 (NBER WP 20171: https://www.nber.org/papers/w20171)
16. Simonov, A., Nosko, C., Rao, J. M. (2018). Competition and Crowd-Out for Brand Keywords in Sponsored Search. Marketing Science 37(2): 200-215. https://doi.org/10.1287/mksc.2017.1065
17. Lewis, R. A., Rao, J. M. (2015). The Unfavorable Economics of Measuring the Returns to Advertising. Quarterly Journal of Economics 130(4): 1941-1973. https://doi.org/10.1093/qje/qjv023
18. Gordon, B. R., Zettelmeyer, F., Bhargava, N., Chapsky, D. (2019). A Comparison of Approaches to Advertising Measurement: Evidence from Big Field Experiments at Facebook. Marketing Science 38(2): 193-225. https://doi.org/10.1287/mksc.2018.1135 (MSI WP 18-113: https://thearf-org-unified-admin.s3.amazonaws.com/MSI_Report_18-113.pdf)
19. Johnson, G. A., Lewis, R. A., Nubbemeyer, E. I. (2017). Ghost Ads: Improving the Economics of Measuring Online Ad Effectiveness. Journal of Marketing Research 54(6): 867-884. https://doi.org/10.1509/jmr.15.0297
20. Johnson, G. A., Lewis, R. A., Nubbemeyer, E. I. (2015). The Online Display Ad Effectiveness Funnel & Carryover: Lessons from 432 Field Experiments. SSRN. https://doi.org/10.2139/ssrn.2701578
21. Rolnick, D., Aydin, K., Pouget-Abadie, J., Kamali, S., Mirrokni, V., Najmi, A. (2019). Randomized Experimental Design via Geographic Clustering. Proceedings of KDD 2019: 2745-2753. https://doi.org/10.1145/3292500.3330778
22. Benjamini, Y., Hochberg, Y. (1995). Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing. Journal of the Royal Statistical Society Series B 57(1): 289-300. https://doi.org/10.1111/j.2517-6161.1995.tb02031.x
23. Google Ads Help. Strengthen media measurement and ROI clarity with incrementality testing improvements (November 11, 2025). https://support.google.com/google-ads/answer/16719772
24. Google Ads Help. Set up Conversion Lift based on users. https://support.google.com/google-ads/answer/12005564
25. Google Ads Help. Set up Conversion Lift based on geography. https://support.google.com/google-ads/answer/14097193
26. Google Ads Help. Comparing Lift measurement types. https://support.google.com/google-ads/answer/14097991
27. Google Ads Help. About advanced location options. https://support.google.com/google-ads/answer/1722038
28. Google Ads API release notes, v25.1 (2026-08-19). https://developers.google.com/google-ads/api/docs/release-notes
29. Meta Business Help Center. Brand Lift minimum requirements. https://www.facebook.com/business/help/417527072254206
30. Meta Business Help Center. About Brand Lift tests. https://www.facebook.com/business/help/1693381447650068
31. Meta Business Help Center. About confidence in your tests and experiments. https://www.facebook.com/business/help/239549606692303
32. Meta Business Help Center. About Facebook-managed tests. https://www.facebook.com/business/help/453968412201452
33. Meta Business Help Center. Best practices to get started with Experiments. https://www.facebook.com/business/help/2420136524735942
34. Meta for Developers. Ad Study (Marketing API reference). https://developers.facebook.com/docs/marketing-api/reference/ad-study
35. Meta for Developers. Ads MCP Server overview. https://developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/ads-mcp-server-overview
36. CausalImpact R package documentation. https://google.github.io/CausalImpact/CausalImpact.html
