
| **概念**        | **描述**                                           |
|-----------------|----------------------------------------------------|
| **cuDNN** **TensorRT**      | NVIDIA深度学习加速库，优化神经网络**工具本身**  |
| **CUDA**        | NVIDIA 利用 GPU 加速计算。 **工具箱**   |
| **TensorFlow** **PyTorch**  | 机器学习框架**建筑蓝图包含工具箱**    |
| **Conda**  **Chocolatey (choco)**     | 包管理和环境管理工具，用于创建和管理虚拟环境。 **工具箱架子**   |
| **环境变量**     | 指引系统找工具和库   **路线图** |




![](d:/BaiduSyncdisk/DyVault/Notes/Diffusion/images/2024-12-31-15-14-44.png)


**卷积层**：提取输入数据特征的神经网络层。
**梯度**：描述损失函数变化率的数学工具，推动模型优化。
| 概念         | 比喻                                   | 作用                                      | 常用文件名称       | 文件格式说明       |
|--------------|----------------------------------------|-------------------------------------------|--------------------|--------------------|
| 权重         | 果汁中水果和水的比例                   | 决定最终的味道                            | weights.npy        | NumPy 数组文件，用于存储权重值 |
| 卷积层       | 制作果汁时使用的工具                   | 提取输入数据的不同特征                  | conv_layer.py      | Python 文件，定义卷积层的实现 |
| 潜在空间     | 所有果汁汇聚的大碗                     | 表示不同果汁的特征                       | latent_space.pkl    | Pickle 文件，存储潜在空间的特征 |
| 梯度         | 调整果汁味道的过程                     | 指导如何改进配方，以减少损失             | gradients.csv       | CSV 文件，记录梯度值和更新信息 |
