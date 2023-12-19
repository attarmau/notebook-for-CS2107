# notebook-for-CS2107
Hands-on information security technique for engineer in reality

- NEVER ASSUME THAT THINGS ARE SECURE. INSTEAD, ASSUME THE OPPOSITE, AND PROVE THEM TO BE SECURE.
- FOCUS ON YOUR NEEDS ON SECURITY
- BE PROCATIVE
<img width="617" alt="截圖 2023-04-07 上午7 42 27" src="https://user-images.githubusercontent.com/87364730/230513038-d5889ebf-28f6-49b2-879b-6e4df8e151fb.png">

classification:
類別變數: https://varsellcm.r-forge.r-project.org/
數值變數：kmeans

res_with2 <- VarSelCluster(df_model_sub, vbleSelec = F, gvals = 5,
                    crit.varsel = 'BIC, nbcores = 5)
###res_with2 %>% saveRDS('mod/mod_5_Q + 單價G.rds')

結果可以用shiny看
VarSelShiny(res_with2)

取分群用這個
res_with2@partitions@zMAP
