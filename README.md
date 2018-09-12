# Hisat-RNAseq-pipeline
### 缘起

>  2018年9月12日，hyp在学习全基因组RNAseq流程，我便整理此流程希望能有帮助

### 我的预期
适用范围：
该pipeline目前只适用Pair end双端测序数据

只需要配置相关软件：

- 此pipeline需要用到的软件
  - fastp
  - hisat

指定输入数据文件夹和输出数据文件夹：

- --input
- --output

即可获得：

- 数据质控结果&图

- 差异基因列表&图

### 脚本工作流程

1. 去除reads左侧13个碱基（此处为低质量序列）
   - 有的地方也去除了右侧3碱基	
2. 去除低质量的reads，基于`Q20, Q30`
3. hisat mapping
4. sort
5. hisat 求差异基因
   - 绘图

