from typing import Optional

from sqlalchemy import BigInteger, CHAR, Integer, PrimaryKeyConstraint, SmallInteger, String, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime

class Base(DeclarativeBase):
    pass


class TDictCustomer(Base):
    __tablename__ = 't_dict_customer'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey6'),
        {'comment': '客户信息表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    name_cn: Mapped[str] = mapped_column(String(100), comment='客户中文名称')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='所属应用ID，关联应用表')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    name_en: Mapped[Optional[str]] = mapped_column(String(100), comment='客户英文名称')


class TDictLargeModel(Base):
    __tablename__ = 't_dict_large_model'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey7'),
        {'comment': '大模型表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    base_url: Mapped[str] = mapped_column(String(255), comment='API基础地址')
    api_key: Mapped[str] = mapped_column(String(255), comment='API访问密钥（加密存储）')
    model_name: Mapped[str] = mapped_column(String(100), comment='模型名称')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='所属应用id')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')


class TDictPromptTag(Base):
    __tablename__ = 't_dict_prompt_tag'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey9'),
        {'comment': '提示词标签表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    tag_name: Mapped[str] = mapped_column(String(100), comment='标签名称')
    tag_code: Mapped[str] = mapped_column(String(100), comment='标签编码')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')


class TDictPromptTemplateType(Base):
    __tablename__ = 't_dict_prompt_template_type'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey10'),
        {'comment': '提示词模板类型表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    template_type_name: Mapped[str] = mapped_column(String(255), comment='模板类型名称（如"混沌"、"应急"）')
    template_type_code: Mapped[str] = mapped_column(String(255), comment='模板类型编码')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')


class TDictProtocolType(Base):
    __tablename__ = 't_dict_protocol_type'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey8'),
        {'comment': '协议类型表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    protocol_name: Mapped[str] = mapped_column(String(100), comment='协议名称（如mcp、function call）')
    protocol_code: Mapped[str] = mapped_column(String(100), comment='协议类型编码（枚举映射）')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')


class TMemoryEntryPlan(Base):
    __tablename__ = 't_memory_entry_plan'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_copy1_pkey'),
        {'comment': '应用入口规划表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    business_module_id: Mapped[str] = mapped_column(CHAR(32), comment='业务模块ID')
    sequence_no: Mapped[int] = mapped_column(Integer, comment='执行顺序号')
    is_enabled: Mapped[int] = mapped_column(SmallInteger, comment='是否启用')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    module_flow_id: Mapped[Optional[str]] = mapped_column(CHAR(32), comment='模块流程ID（关联模块流程设置表）')
    module_flow_name: Mapped[Optional[str]] = mapped_column(String(100), comment='模块流程中文名称')
    enabled_time: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP(precision=6), comment='启用时间')
    enabled_user_id: Mapped[Optional[str]] = mapped_column(CHAR(32), comment='启用人id')


class TMemoryFactSummary(Base):
    __tablename__ = 't_memory_fact_summary'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey27'),
        {'comment': '事实摘要表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    start_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=6), comment='事实信息生成起始时间')
    fact_type: Mapped[str] = mapped_column(String(64), comment='事实类型（如"用户信息"、"订单状态"）')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    end_time: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP(precision=6), comment='事实信息生成结束时间')
    fact_text: Mapped[Optional[str]] = mapped_column(Text, comment='事实信息具体内容')
    related_node_id: Mapped[Optional[str]] = mapped_column(CHAR(32), comment='关联的节点ID')
    session_id: Mapped[Optional[str]] = mapped_column(CHAR(32), comment='关联的会话id')


class TMemoryIntentRule(Base):
    __tablename__ = 't_memory_intent_rule'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='t_permission_organization_copy1_pkey1'),
        {'comment': '应用入口意图识别规则表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    rule_type: Mapped[int] = mapped_column(SmallInteger, comment='规则类型（1=RAG，2=智能体）')
    rule_config: Mapped[str] = mapped_column(Text, comment='规则内容（JSON或YAML字符串）')
    is_enabled: Mapped[int] = mapped_column(SmallInteger, comment='是否启用')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    business_type: Mapped[Optional[int]] = mapped_column(SmallInteger, comment='业务类型（1=混沌，2=应急）')
    enabled_time: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP(precision=6), comment='启用时间')


class TMemoryMessage(Base):
    __tablename__ = 't_memory_message'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey26'),
        {'comment': '消息表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    send_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=6), comment='消息发送时间')
    sender: Mapped[str] = mapped_column(String(255), comment='发送者标识（用户/系统/智能体角色）')
    message_content: Mapped[str] = mapped_column(Text, comment='消息具体内容')
    message_type: Mapped[str] = mapped_column(String(32), comment='消息类型（markdown/图片/语音/视频/表情/按钮/代码）')
    session_id: Mapped[str] = mapped_column(CHAR(32), comment='关联会话ID')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    role_name: Mapped[Optional[str]] = mapped_column(String(255), comment='发送者对应的角色名称（如"客服助手"）')
    message_block_type_id: Mapped[Optional[str]] = mapped_column(CHAR(32), comment='消息块类型ID')


class TMemorySession(Base):
    __tablename__ = 't_memory_session'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey25'),
        {'comment': '会话表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    start_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=6), comment='会话开始时间')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    end_time: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP(precision=6), comment='会话结束时间')
    business_id: Mapped[Optional[str]] = mapped_column(String(100), comment='业务ID（关联事件唯一标识），系统对接唯一标识')
    initiator: Mapped[Optional[str]] = mapped_column(String(255), comment='会话发起者（如用户名、系统标识）')
    status: Mapped[Optional[int]] = mapped_column(SmallInteger, comment='会话状态：1-进行中，0-已结束')


class TPermissionApplication(Base):
    __tablename__ = 't_permission_application'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='t_permission_tenant_copy1_pkey'),
        {'comment': '应用管理表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    tenant_id: Mapped[str] = mapped_column(CHAR(32), comment='租户id')
    name_cn: Mapped[str] = mapped_column(String(100), comment='应用名称')
    app_code: Mapped[str] = mapped_column(String(100), comment='应用编码')
    description: Mapped[str] = mapped_column(String(500), comment='应用描述')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(32), comment='是否删除（0表示未删除，非0表示删除）')
    name_en: Mapped[Optional[str]] = mapped_column(String(255), comment='应用英文名')


class TPermissionDepartment(Base):
    __tablename__ = 't_permission_department'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey1'),
        {'comment': '部门管理表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    org_id: Mapped[str] = mapped_column(CHAR(32), comment='组织架构id')
    dept_name: Mapped[str] = mapped_column(String(100), comment='部门名称')
    dept_code: Mapped[str] = mapped_column(String(100), comment='部门编码')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    parent_id: Mapped[Optional[str]] = mapped_column(CHAR(32), comment='父节点id')
    description: Mapped[Optional[str]] = mapped_column(String(500), comment='部门描述')


class TPermissionOrganization(Base):
    __tablename__ = 't_permission_organization'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey'),
        {'comment': '组织架构表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    org_name: Mapped[str] = mapped_column(String(255), comment='组织名称')
    org_code: Mapped[str] = mapped_column(String(255), comment='组织编码')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    parent_id: Mapped[Optional[str]] = mapped_column(CHAR(32), comment='父节点id')
    description: Mapped[Optional[str]] = mapped_column(String(500), comment='描述')


class TPermissionResource(Base):
    __tablename__ = 't_permission_resource'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey5'),
        {'comment': '资源信息管理表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    resource_type: Mapped[int] = mapped_column(SmallInteger, comment='资源类型: 1-菜单, 2-按钮, 3-特定, 4-接口')
    resource_name: Mapped[str] = mapped_column(String(100), comment='资源名称')
    resource_code: Mapped[str] = mapped_column(String(100), comment='资源代码')
    sort_order: Mapped[int] = mapped_column(Integer, comment='排序号')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    resource_path: Mapped[Optional[str]] = mapped_column(String(500), comment='资源路径')
    parent_id: Mapped[Optional[str]] = mapped_column(CHAR(32), comment='父节点id')
    is_visible: Mapped[Optional[int]] = mapped_column(SmallInteger, comment='是否可见')


class TPermissionRole(Base):
    __tablename__ = 't_permission_role'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey3'),
        {'comment': '角色信息管理表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    role_name: Mapped[str] = mapped_column(String(100), comment='角色名称')
    role_code: Mapped[str] = mapped_column(String(100), comment='角色编码')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    description: Mapped[Optional[str]] = mapped_column(String(500), comment='角色描述')
    is_system: Mapped[Optional[int]] = mapped_column(SmallInteger, comment='是否系统内置角色(\x7f（1.是  0.否）')


class TPermissionRoleResourceRel(Base):
    __tablename__ = 't_permission_role_resource_rel'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='t_permission_user_role_rel_copy1_pkey'),
        UniqueConstraint('app_id', 'role_id', 'resource_id', name='t_permission_user_role_rel_copy1_app_id_user_id_role_id_key'),
        {'comment': '角色-资源关联表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    role_id: Mapped[str] = mapped_column(CHAR(32), comment='角色id')
    resource_id: Mapped[str] = mapped_column(CHAR(32), comment='资源id')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')


class TPermissionTenant(Base):
    __tablename__ = 't_permission_tenant'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='租户信息表_pkey'),
        {'comment': '租户信息表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    tenant_name: Mapped[str] = mapped_column(String(100), comment='租户名称')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(32), comment='是否删除（0表示未删除，非0表示删除）')
    tenant_description: Mapped[Optional[str]] = mapped_column(String(500), comment='租户描述')


class TPermissionUser(Base):
    __tablename__ = 't_permission_user'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey2'),
        {'comment': '用户信息表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    username: Mapped[str] = mapped_column(String(100), comment='用户名')
    password: Mapped[str] = mapped_column(String(500), comment='用户密码')
    status: Mapped[int] = mapped_column(SmallInteger, comment='用户状态: 1-正常, 0-禁用')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    dept_id: Mapped[Optional[str]] = mapped_column(CHAR(32), comment='部门id')
    position: Mapped[Optional[str]] = mapped_column(String(100), comment='岗位名称')
    email: Mapped[Optional[str]] = mapped_column(String(100), comment='邮箱')
    phone: Mapped[Optional[str]] = mapped_column(String(100), comment='手机号')


class TPermissionUserRoleRel(Base):
    __tablename__ = 't_permission_user_role_rel'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey4'),
        UniqueConstraint('app_id', 'user_id', 'role_id', name='unique_dex'),
        {'comment': '用户-角色关联表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    user_id: Mapped[str] = mapped_column(CHAR(32), comment='用户id')
    role_id: Mapped[str] = mapped_column(CHAR(32), comment='角色id')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')


class TRagCategory(Base):
    __tablename__ = 't_rag_category'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_copy1_pkey3'),
        {'comment': '知识库分类表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    name_cn: Mapped[str] = mapped_column(String(100), comment='分类中文名称（如产品手册）')
    level: Mapped[int] = mapped_column(SmallInteger, comment='分类层级（如1级、2级）')
    sort_order: Mapped[int] = mapped_column(Integer, comment='排序号')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    name_en: Mapped[Optional[str]] = mapped_column(String(100), comment='分类英文名称（如ProductManual）')
    parent_id: Mapped[Optional[str]] = mapped_column(CHAR(32), comment='父节点id')
    tags: Mapped[Optional[dict]] = mapped_column(JSONB, comment='所属标签（JSON数组存储标签ID或名称）')


class TRagFactSummary(Base):
    __tablename__ = 't_rag_fact_summary'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='t_memory_fact_summary_copy1_pkey'),
        {'comment': '知识库事实摘要表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    start_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=6), comment='事实信息生成起始时间')
    fact_type: Mapped[str] = mapped_column(String(64), comment='事实类型')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    end_time: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP(precision=6), comment='事实信息生成结束时间')
    fact_text: Mapped[Optional[str]] = mapped_column(Text, comment='事实信息具体内容')
    related_node_id: Mapped[Optional[str]] = mapped_column(CHAR(32), comment='关联的节点ID')
    kg_id: Mapped[Optional[str]] = mapped_column(CHAR(32), comment='关联知识图谱ID')


class TRagGraph(Base):
    __tablename__ = 't_rag_graph'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_copy1_pkey6'),
        {'comment': '知识图谱表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    file_id: Mapped[str] = mapped_column(CHAR(32), comment='原始文件ID')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    kg_result: Mapped[dict] = mapped_column(JSONB, comment='知识图谱结果（实体、关系等）')
    extract_time: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP(precision=6), comment='提取时间')


class TRagIntentRule(Base):
    __tablename__ = 't_rag_intent_rule'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_copy1_pkey1'),
        {'comment': '知识库入口意图识别规则表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    rule_condition: Mapped[str] = mapped_column(Text, comment='规则条件（如"意图包含\'查询资料\'"）')
    rule_name: Mapped[str] = mapped_column(String(100), comment='规则名称（如"知识库查询意图规则"）')
    is_enabled: Mapped[int] = mapped_column(SmallInteger, comment='是否启用')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    destination: Mapped[Optional[str]] = mapped_column(String(255), comment='规则目的地（跳转的目标）')
    enabled_time: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP(precision=6), comment='启用时间')
    enabled_user_id: Mapped[Optional[str]] = mapped_column(CHAR(32), comment='启用人')


class TRagMessage(Base):
    __tablename__ = 't_rag_message'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_copy1_pkey5'),
        {'comment': '知识库消息表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    send_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=6), comment='发送时间')
    sender: Mapped[str] = mapped_column(String(255), comment='发送者')
    message_content: Mapped[str] = mapped_column(Text, comment='消息内容')
    message_type: Mapped[str] = mapped_column(String(32), comment='消息类型（markdown/图片/语音等）')
    rag_session_id: Mapped[str] = mapped_column(CHAR(32), comment='知识库会话id')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    role_name: Mapped[Optional[str]] = mapped_column(String(100), comment='可见角色')
    file_id: Mapped[Optional[str]] = mapped_column(CHAR(32), comment='引用的原始文件ID')


class TRagOriginalFile(Base):
    __tablename__ = 't_rag_original_file'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_copy1_pkey2'),
        {'comment': '知识库原始文件表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    minio_url: Mapped[str] = mapped_column(String(500), comment='MinIO存储地址')
    original_name: Mapped[str] = mapped_column(String(255), comment='原始文件名称（含扩展名）')
    category_id: Mapped[str] = mapped_column(CHAR(32), comment='所属分类id')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    file_size: Mapped[Optional[int]] = mapped_column(BigInteger, comment='文件大小（字节）')
    file_type: Mapped[Optional[str]] = mapped_column(String(64), comment='文件类型（如pdf、docx）')


class TRagSession(Base):
    __tablename__ = 't_rag_session'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_copy1_copy1_pkey'),
        {'comment': '知识库会话表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    start_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=6), comment='开始时间')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    end_time: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP(precision=6), comment='结束时间（未结束为null）')
    business_id: Mapped[Optional[str]] = mapped_column(CHAR(32), comment='业务ID')
    initiator: Mapped[Optional[str]] = mapped_column(String(255), comment='启动者')
    status: Mapped[Optional[int]] = mapped_column(SmallInteger, comment='会话状态（1-进行中，0-已结束）')


class TRagTag(Base):
    __tablename__ = 't_rag_tag'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_copy1_pkey4'),
        {'comment': '知识库标签表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    name_cn: Mapped[str] = mapped_column(String(100), comment='标签中文名称（如新品、故障排除）')
    name_en: Mapped[str] = mapped_column(String(100), comment='标签英文名称')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    tag_code: Mapped[Optional[str]] = mapped_column(String(64), comment='标签编码')


class TRagVector(Base):
    __tablename__ = 't_rag_vector'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_copy1_pkey7'),
        {'comment': '组织架构表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    file_id: Mapped[str] = mapped_column(CHAR(32), comment='原始文件ID')
    vector_result: Mapped[dict] = mapped_column(JSONB, comment='分块向量结果（含文本块、milvus索引）')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    chunk_count: Mapped[Optional[str]] = mapped_column(CHAR(32), comment='分块数量')
    vector_time: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP(precision=6), comment='向量化时间')


class TSettingAgentProduct(Base):
    __tablename__ = 't_setting_agent_product'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey18'),
        {'comment': '智能体产品表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    vendor_name: Mapped[str] = mapped_column(String(128), comment='厂家名称')
    product_name: Mapped[str] = mapped_column(String(32), comment='产品名称（adk/dify/autogen/agno）')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')


class TSettingMessageBlockType(Base):
    __tablename__ = 't_setting_message_block_type'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey17'),
        {'comment': '消息块类型表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    has_markdown: Mapped[Optional[int]] = mapped_column(SmallInteger, comment='是否包含markdown文本')
    has_image: Mapped[Optional[int]] = mapped_column(SmallInteger, comment='是否包含图片')
    has_audio: Mapped[Optional[int]] = mapped_column(SmallInteger, comment='是否包含语音')
    has_video: Mapped[Optional[int]] = mapped_column(SmallInteger, comment='是否包含视频')
    has_emoji: Mapped[Optional[int]] = mapped_column(SmallInteger, comment='是否包含表情')
    has_button: Mapped[Optional[int]] = mapped_column(SmallInteger, comment='是否包含按钮')
    has_code: Mapped[Optional[int]] = mapped_column(SmallInteger, comment='是否包含代码')


class TSettingPrompt(Base):
    __tablename__ = 't_setting_prompt'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey11'),
        {'comment': '提示词表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    name_cn: Mapped[str] = mapped_column(String(100), comment='提示词中文名')
    content: Mapped[str] = mapped_column(Text, comment='提示词内容')
    tag_id: Mapped[str] = mapped_column(CHAR(32), comment='提示词标签')
    version: Mapped[str] = mapped_column(String(100), comment='版本号(1.0.0)')
    is_enabled: Mapped[int] = mapped_column(SmallInteger, comment='是否启用')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    name_en: Mapped[Optional[str]] = mapped_column(String(100), comment='提示词英文名')
    enabled_time: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP(precision=6), comment='启用时间')
    workflow_node_id: Mapped[Optional[str]] = mapped_column(CHAR(32), comment='所属节点Id')


class TSettingPromptTemplate(Base):
    __tablename__ = 't_setting_prompt_template'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey15'),
        {'comment': '提示词模板表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    submit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='提交人')
    submit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=6), comment='提交时间')
    template_name: Mapped[str] = mapped_column(String(100), comment='提示词模板名称')
    template_content: Mapped[str] = mapped_column(Text, comment='提示词模板内容')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    trainer: Mapped[Optional[str]] = mapped_column(String(64), comment='训练提供者（如DSPy）')
    prompt_type: Mapped[Optional[str]] = mapped_column(String(64), comment='提示词类型')
    tag_id: Mapped[Optional[str]] = mapped_column(CHAR(32), comment='所属提示词标签ID')


class TSettingSkill(Base):
    __tablename__ = 't_setting_skill'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey12'),
        {'comment': '技能信息表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    name_cn: Mapped[str] = mapped_column(String(100), comment='技术中文名')
    name_en: Mapped[str] = mapped_column(String(100), comment='技术英文名')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    input_params: Mapped[Optional[dict]] = mapped_column(JSONB, comment='输入参数')
    return_value: Mapped[Optional[dict]] = mapped_column(JSONB, comment='返回值')
    function_body: Mapped[Optional[str]] = mapped_column(Text, comment='函数体')


class TSettingSystemConfig(Base):
    __tablename__ = 't_setting_system_config'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey16'),
        {'comment': '系统设置表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    message_window_count: Mapped[int] = mapped_column(Integer, comment='消息时间窗口次数')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')


class TSettingThoughtType(Base):
    __tablename__ = 't_setting_thought_type'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey14'),
        {'comment': '思考类型表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    thought_name: Mapped[str] = mapped_column(String(100), comment='思考名称')
    thought_type: Mapped[str] = mapped_column(String(100), comment='思考类型（pdca/执行监督/思维链/ReAct/MDP）')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    suggested_prompt: Mapped[Optional[str]] = mapped_column(Text, comment='建议提示词')


class TSettingWorkflow(Base):
    __tablename__ = 't_setting_workflow'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey13'),
        {'comment': '工作流集合表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    flow_name: Mapped[str] = mapped_column(String(100), comment='工作流名称')
    is_standard: Mapped[int] = mapped_column(SmallInteger, comment='是否标准工作流（1.是  0.否）')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')


class TWorkflow(Base):
    __tablename__ = 't_workflow'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey21'),
        {'comment': '工作流表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    workflow_name: Mapped[str] = mapped_column(String(100), comment='工作流名称（应用-业务-功能三级命名）')
    node_id: Mapped[str] = mapped_column(CHAR(32), comment='关联节点业务id')
    config_id: Mapped[str] = mapped_column(CHAR(32), comment='关联工作流配置ID')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    condition: Mapped[Optional[str]] = mapped_column(Text, comment='触发节点的条件表达式（如amount>1000）')
    node_order: Mapped[Optional[int]] = mapped_column(Integer, comment='节点顺序（用于排序）')
    target_node_id: Mapped[Optional[str]] = mapped_column(CHAR(32), comment='下一个跳转的节点id')
    exit_condition: Mapped[Optional[str]] = mapped_column(Text, comment="工作流终止的条件表达式（如status='success'）")


class TWorkflowBusinessModule(Base):
    __tablename__ = 't_workflow_business_module'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey19'),
        {'comment': '业务模块表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    business_name: Mapped[str] = mapped_column(String(100), comment='业务名称（如支付、库存、发货等）')
    business_code: Mapped[str] = mapped_column(String(100), comment='业务模块编码')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    description: Mapped[Optional[str]] = mapped_column(String(500), comment='业务模块描述')


class TWorkflowConfig(Base):
    __tablename__ = 't_workflow_config'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey20'),
        {'comment': '工作流配置表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    version: Mapped[str] = mapped_column(String(32), comment='版本号（如v1.0.0）')
    dsl_config: Mapped[dict] = mapped_column(JSONB, comment='工作流DSL配置（包含流程、节点、大模型等信息）')
    is_enabled: Mapped[int] = mapped_column(SmallInteger, comment='是否启用')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    enabled_time: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP(precision=6), comment='启用时间')


class TWorkflowModuleSetting(Base):
    __tablename__ = 't_workflow_module_setting'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey23'),
        {'comment': '模块流程设置表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    name_cn: Mapped[str] = mapped_column(String(100), comment='模块流程中文名称')
    name_en: Mapped[str] = mapped_column(String(100), comment='模块流程英文名称')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    workflow_chain: Mapped[Optional[str]] = mapped_column(Text, comment='工作流链（如payment_flow>>inventory_flow）')
    is_enabled: Mapped[Optional[int]] = mapped_column(SmallInteger, comment='是否启用（预留）')
    enabled_time: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP(precision=6), comment='启用时间（预留）')


class TWorkflowNode(Base):
    __tablename__ = 't_workflow_node'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey22'),
        {'comment': '工作流节点表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    name_cn: Mapped[str] = mapped_column(String(100), comment='节点中文名称（如用户意图识别节点）')
    name_en: Mapped[str] = mapped_column(String(100), comment='节点英文名')
    node_code: Mapped[str] = mapped_column(String(100), comment='节点唯一编码')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    agent_product_id: Mapped[Optional[str]] = mapped_column(CHAR(32), comment='能体产品ID')
    llm_model_id: Mapped[Optional[str]] = mapped_column(CHAR(32), comment='大模型ID')
    prompt_id: Mapped[Optional[str]] = mapped_column(CHAR(32), comment='提示词ID')


class TWorkflowSharedVariable(Base):
    __tablename__ = 't_workflow_shared_variable'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='template_copy1_pkey24'),
        {'comment': '共享变量表'}
    )

    id: Mapped[str] = mapped_column(CHAR(32), primary_key=True, comment='主键')
    app_id: Mapped[str] = mapped_column(CHAR(32), comment='应用id')
    variable_key: Mapped[str] = mapped_column(String(255), comment='变量键（应用.工作流.节点.键名格式）')
    node_id: Mapped[str] = mapped_column(CHAR(32), comment='节点ID（关联节点表主键）')
    assigned_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=6), comment='最后一次赋值的时间')
    create_user_id: Mapped[str] = mapped_column(CHAR(32), comment='创建者')
    create_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='创建时间')
    edit_user_id: Mapped[str] = mapped_column(CHAR(32), comment='最后更新人')
    edit_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(precision=0), comment='更新时间')
    is_deleted: Mapped[str] = mapped_column(String(255), comment='是否删除（0表示未删除，非0表示删除）')
    variable_value: Mapped[Optional[str]] = mapped_column(Text, comment='变量值')
    node_stage: Mapped[Optional[str]] = mapped_column(String(16), comment='节点阶段（前/中/后）')
