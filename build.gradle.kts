
import org.jetbrains.kotlin.gradle.tasks.KotlinCompile
import org.jlleitschuh.gradle.ktlint.KtlintExtension

plugins {
	id("org.springframework.boot") version "3.2.1"
	id("io.spring.dependency-management") version "1.1.4"
	kotlin("jvm") version "1.9.21"
	kotlin("plugin.spring") version "1.9.21"
	id("me.champeau.jmh") version "0.7.2"
	id("org.jlleitschuh.gradle.ktlint") version "11.3.1"
	id("org.jetbrains.kotlin.plugin.allopen") version "1.9.21"
}

group = "com.letsbe"
version = "0.0.1-SNAPSHOT"

java {
	sourceCompatibility = JavaVersion.VERSION_17
}

repositories {
	mavenCentral()
}

dependencies {
	implementation("org.springframework.boot:spring-boot-starter")
	implementation("org.jetbrains.kotlin:kotlin-reflect")
	testImplementation("org.springframework.boot:spring-boot-starter-test")
	testImplementation("org.openjdk.jmh:jmh-core:1.37")
	testImplementation("org.openjdk.jmh:jmh-generator-annprocess:1.37")
}

tasks.withType<KotlinCompile> {
	kotlinOptions {
		freeCompilerArgs += "-Xjsr305=strict"
		jvmTarget = "17"
	}
}

tasks.withType<Test> {
	useJUnitPlatform()
}

configure<KtlintExtension> {
	filter {
		exclude {
			it.file.path.contains("generated")
		}
	}
}

jmh {
	// Configure the list of JMH benchmarks to run
	fork = 1
	iterations = 1
	threads = 1
	timeUnit = "ms"
	warmupIterations = 3
}

allOpen {
	// final classes are not open by default
	annotation("org.openjdk.jmh.annotations.State")
}
